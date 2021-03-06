{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "184d2066",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (Temp/ipykernel_12084/1747616957.py, line 38)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\user\\AppData\\Local\\Temp/ipykernel_12084/1747616957.py\"\u001b[1;36m, line \u001b[1;32m38\u001b[0m\n\u001b[1;33m    def print_data(ds):\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from zipfile import ZipFile\n",
    "from io import BytesIO\n",
    "import pandas as pd\n",
    "from datetime import timedelta\n",
    "from datetime import datetime\n",
    "\n",
    "from airflow import DAG\n",
    "from airflow.operators.python import PythonOperator\n",
    "\n",
    "TOP_1M_DOMAINS = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'\n",
    "TOP_1M_DOMAINS_FILE = 'top-1m.csv'\n",
    "\n",
    "\n",
    "def get_data():\n",
    "    top_doms = requests.get(TOP_1M_DOMAINS, stream=True)\n",
    "    zipfile = ZipFile(BytesIO(top_doms.content))\n",
    "    top_data = zipfile.read(TOP_1M_DOMAINS_FILE).decode('utf-8')\n",
    "\n",
    "    with open(TOP_1M_DOMAINS_FILE, 'w') as f:\n",
    "        f.write(top_data)\n",
    "\n",
    "\n",
    "def get_top_10_dom():\n",
    "    top_data_df = pd.read_csv('TOP_1M_DOMAINS', names=['rank', 'domain'])\n",
    "    top_data_df['dom'] = top_data_df.domain.str.split('.').apply(lambda x: x[1])\n",
    "    top_data_10_dom = top_data_df.groupby('dom')\\\n",
    "               .agg({'domain': 'count'})\\\n",
    "               .sort_values('domain', ascending=False)\\\n",
    "               .head(10)\n",
    "    \n",
    "    with open ('top_data_10_dom.csv', 'w') as f:\n",
    "        f.write(top_data_10_dom.to_csv(index=False, header=False))\n",
    "        \n",
    "        \n",
    "def get_biggest_domain_len():\n",
    "    top_data_df = pd.read_csv('TOP_1M_DOMAINS', names=['rank', 'domain'])\n",
    "    top_data_df['length'] = top_data_df.domain.apply(lambda x: len(x))\n",
    "    get_biggest_domain_len = top_data_df.sort_values(['length', 'domain'], ascending=False)\\\n",
    "               .domain.head(1)\\\n",
    "               .to_list()[0]\n",
    "    \n",
    "    with open('get_biggest_domain_len.txt', 'w') as f:\n",
    "        f.write(get_biggest_domain_len)\n",
    "        \n",
    "def get_rank_airflow():\n",
    "    top_data_df = pd.read_csv('TOP_1M_DOMAINS', names=['rank', 'domain'])\n",
    "    position = top_data_df.query('domain == \"airflow.com\"').rank.to_list(0)\n",
    "    if position == '':\n",
    "        position = 'not found'\n",
    "    \n",
    "    with open('get_rank_airflow.txt', 'w') as f:\n",
    "        f.write(position)\n",
    "\n",
    "def print_data(ds):\n",
    "    with open('top_data_10_dom.csv', 'r') as f:\n",
    "        all_data = f.read()\n",
    "    with open('get_biggest_domain_len.txt', 'r') as f:\n",
    "        all_data_biggest = f.read()\n",
    "    with open('get_rank_airflow.txt', 'r') as f:\n",
    "        all_data_airflow = f.read()\n",
    "        \n",
    "    date = ds\n",
    "\n",
    "    print(f'Top 10 domains for date {date}')\n",
    "    print(all_data)\n",
    "\n",
    "    print(f'Biggest domain length for date {date}')\n",
    "    print(all_data_biggest)\n",
    "    \n",
    "    print(f'Airflow.com rank for date {date}')\n",
    "    print(all_data_airflow)\n",
    "\n",
    "\n",
    "default_args = {\n",
    "    'owner': 'a.eliseyev',\n",
    "    'depends_on_past': False,\n",
    "    'retries': 2,\n",
    "    'retry_delay': timedelta(minutes=5),\n",
    "    'start_date': datetime(2022, 1, 26),\n",
    "    'schedule_interval': '0 12 * * *'\n",
    "}\n",
    "\n",
    "dag = DAG('top_10_length_airflow', default_args=default_args)\n",
    "\n",
    "t1 = PythonOperator(task_id='get_data',\n",
    "                    python_callable=get_data,\n",
    "                    dag=dag)\n",
    "\n",
    "t2 = PythonOperator(task_id='get_top_10_dom',\n",
    "                    python_callable=get_stat,\n",
    "                    dag=dag)\n",
    "\n",
    "t2_length = PythonOperator(task_id='get_biggest_domain_len',\n",
    "                        python_callable=get_stat_com,\n",
    "                        dag=dag)\n",
    "\n",
    "t2_airflow = PythonOperator(task_id='get_rank_airflow',\n",
    "                        python_callable=get_stat_com,\n",
    "                        dag=dag)\n",
    "\n",
    "t3 = PythonOperator(task_id='print_data',\n",
    "                    python_callable=print_data,\n",
    "                    dag=dag)\n",
    "\n",
    "t1 >> [t2, t2_length, t2_airflow] >> t3\n",
    "\n",
    "#t1.set_downstream(t2)\n",
    "#t1.set_downstream(t2_com)\n",
    "\n",
    "#t2.set_downstream(t3)\n",
    "#t2_com.set_downstream(t3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ccc5e4f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
