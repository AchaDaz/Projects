#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import timedelta
from datetime import datetime
import telegram

from airflow.decorators import dag, task
from airflow.operators.python import get_current_context
from airflow.models import Variable



LINK = 'https://gist.githubusercontent.com/zhonglism/f146a9423e2c975de8d03c26451f841e/raw/f79e190df4225caed58bf360d8e20a9fa872b4ac/vgsales.csv'

VGSALES = 'vgsales.csv'

default_args = {
    'owner': 'a.eliseev',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 1, 27),
    'schedule_interval': '0 12 * * *'
}

CHAT_ID = 1016148585
TOKEN = '2019166088:AAHAH7XcDZPFCAzjkWwSSyzvYC4jXAIgRFA'


def send_message(context):
    date = context['ds']
    dag_id = context['dag'].dag_id
    message = f'Done. Dag {dag_id} completed on {date}'
    
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)



@dag(default_args=default_args, catchup=False)
def stat_airflow_2_vgsales():
    @task(retries=4)
    def get_data():
        vgsales_df = pd.read_csv(LINK)
        vgsales_df.dropna(inplace=True)
        vgsales_df.Year = vgsales_df.Year.apply(int)
        vgsales_2015 = vgsales_df.query('Year == 2015')
        return vgsales_2015

    @task()
    def biggest_sales(vgsales_2015):
        most_sales_world = vgsales_2015.sort_values('Global_Sales', ascending=False)                                       .Name.head(1)                                       .to_list()[0]
        return most_sales_world
    
    @task()
    def europe_vgsales_top(vgsales_2015):
        europe_vgsales = vgsales_2015.groupby('Genre', as_index=False)                                     .agg({'EU_Sales': 'mean'})                                     .sort_values('EU_Sales', ascending=False)                                     .rename(columns={'EU_Sales': 'EU_Sales_mean'})
        europe_vgsales_top1 = europe_vgsales.EU_Sales_mean.head(1)
        europe_vgsales_top = europe_vgsales.query('EU_Sales_mean == @europe_vgsales_top1')

        return europe_vgsales_top
    
    @task()
    def na_vgsales_top(vgsales_2015):
        na_million_df = vgsales_2015.query('NA_Sales > 1.0')
        na_platform = na_million_df.groupby('Platform')                               .agg({'Genre': 'count'})                               .sort_values('Genre', ascending=False)

        na_vgsales_top1 = na_platform.Genre.head(1)
        na_vgsales_top = na_platform.query('Genre == @na_vgsales_top1')

        return na_vgsales_top
    
    @task()
    def jp_sales(vgsales_2015):
        jp_df = vgsales_2015.groupby('Publisher').agg({'JP_Sales': 'mean'})
        jp_df_max = jp_df.JP_Sales.max()
        JP_df_most = jp_df.query('JP_Sales == @jp_df_max')

        return JP_df_most

    @task()
    def eur_vs_jp(vgsales_2015):
        eur_vs_jp_df = vgsales_2015.copy()
        eur_vs_jp_df['diff'] = eur_vs_jp_df.EU_Sales - eur_vs_jp_df.JP_Sales

        eur_vs_jp_df.query('diff > 0').shape[0]

        return eur_vs_jp_df

    @task(on_success_callback=send_message)
    def print_info(most_sales_world,
                   europe_vgsales_top,
                   na_vgsales_top,
                   JP_df_most,
                   eur_vs_jp_df):
        
        context = get_current_context()
      

        
        print(f'''For 2015 year:
            Game with the biggest sales: {most_sales_world},
            The biggest sales in Europe for genre: {europe_vgsales_top},
            The biggest sales per platform with 1kk sales in NA: {na_vgsales_top},
            The biggest sales per publisher in Japan: {JP_df_most},
            The number of games that sold better in Europe than in Japan: {eur_vs_jp_df}''')
        
        
    vgsales_2015 = get_data()
    
    most_sales_world = biggest_sales(vgsales_2015)
    
    europe_vgsales_top = europe_vgsales_top(vgsales_2015)
    
    na_vgsales_top = na_vgsales_top(vgsales_2015)
    
    JP_df_most = jp_sales(vgsales_2015)
    
    eur_vs_jp_df = eur_vs_jp(vgsales_2015)
    
    print_info(most_sales_world,
                   europe_vgsales_top,
                   na_vgsales_top,
                   JP_df_most,
                   eur_vs_jp_df)
    
    
    

stat_airflow_2_vgsales = stat_airflow_2_vgsales()    





















# In[2]:





# In[ ]:




