#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from zipfile import ZipFile
from io import BytesIO
import pandas as pd
from datetime import timedelta
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

TOP_1M_DOMAINS = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
TOP_1M_DOMAINS_FILE = 'top-1m.csv'


def get_data():
    top_doms = pd.read_csv(TOP_1M_DOMAINS, stream=True)
    zipfile = ZipFile(BytesIO(top_doms.content))
    top_data = zipfile.read(TOP_1M_DOMAINS_FILE).decode('utf-8')

    with open(TOP_1M_DOMAINS_FILE, 'w') as f:
        f.write(top_data)


def get_top_10_dom():
    top_data_df = pd.read_csv('TOP_1M_DOMAINS', names=['rank', 'domain'])
    top_data_df['dom'] = top_data_df.domain.str.split('.').apply(lambda x: x[1])
    top_data_10_dom = top_data_df.groupby('dom')               .agg({'domain': 'count'})               .sort_values('domain', ascending=False)               .head(10)
    
    with open ('top_data_10_dom.csv', 'w') as f:
        f.write(top_data_10_dom.to_csv(index=False, header=False))
        
        
def get_biggest_domain_len():
    top_data_df = pd.read_csv('TOP_1M_DOMAINS', names=['rank', 'domain'])
    top_data_df['length'] = top_data_df.domain.apply(lambda x: len(x))
    get_biggest_domain_len = top_data_df.sort_values(['length', 'domain'], ascending=False)               .domain.head(1)               .to_list()[0]
    
    with open('get_biggest_domain_len.txt', 'w') as f:
        f.write(get_biggest_domain_len)
        
def get_rank_airflow():
    top_data_df = pd.read_csv('TOP_1M_DOMAINS', names=['rank', 'domain'])
    position = top_data_df.query('domain == "airflow.com"').rank.to_list(0)
    if position == '':
        position = 'not found'
    
    with open('get_rank_airflow.txt', 'w') as f:
        f.write(position)

def print_data(ds):
    with open('top_data_10_dom.csv', 'r') as f:
        all_data = f.read()
    with open('get_biggest_domain_len.txt', 'r') as f:
        all_data_biggest = f.read()
    with open('get_rank_airflow.txt', 'r') as f:
        all_data_airflow = f.read()
        
    date = ds

    print(f'Top 10 domains for date {date}')
    print(all_data)

    print(f'Biggest domain length for date {date}')
    print(all_data_biggest)
    
    print(f'Airflow.com rank for date {date}')
    print(all_data_airflow)


default_args = {
    'owner': 'a.eliseyev',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 1, 26),
    'schedule_interval': '0 12 * * *'
}

dag = DAG('top_10_length_airflow', default_args=default_args)

t1 = PythonOperator(task_id='get_data',
                    python_callable=get_data,
                    dag=dag)

t2 = PythonOperator(task_id='get_top_10_dom',
                    python_callable=get_top_10_dom,
                    dag=dag)

t2_length = PythonOperator(task_id='get_biggest_domain_len',
                        python_callable=get_biggest_domain_len,
                        dag=dag)

t2_airflow = PythonOperator(task_id='get_rank_airflow',
                        python_callable=get_rank_airflow,
                        dag=dag)

t3 = PythonOperator(task_id='print_data',
                    python_callable=print_data,
                    dag=dag)

t1 >> [t2, t2_length, t2_airflow] >> t3

#t1.set_downstream(t2)
#t1.set_downstream(t2_com)

#t2.set_downstream(t3)
#t2_com.set_downstream(t3)


# In[ ]:




