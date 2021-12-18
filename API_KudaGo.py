import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup

def clear_description(description):
    return BeautifulSoup(description).get_text()

def find_dates(event):
    startdate_dt = datetime.datetime.fromtimestamp(event['dates'][0]['start'])
    enddate_dt = datetime.datetime.fromtimestamp(event['dates'][0]['end'])
    startdate_txt = startdate_dt.strftime('%d-%m-%Y')
    enddate_txt = enddate_dt.strftime('%d-%m-%Y')
    return startdate_dt, enddate_dt, startdate_txt, enddate_txt

def fill_df(event):
    event['description'] = clear_description(event['description'])
    _, _ , start_dt, end_dt = find_dates(event)
    event['start_date'] = start_dt
    event['end_date'] = end_dt
    del event['dates']
    event['url'] = event['site_url']
    del event['site_url']
    return event

def get_data_from_API():
    print('Новый запрос от', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    url = 'https://kudago.com/public-api/v1.4/events/'
    params = '?order_by=-publication_date&location=msk&fields=id,title,dates,description,price,site_url'
    response = requests.get(url+params)
    results = response.json()['results']
    return results

def check_event(event):
    start_dt, end_dt, _, _ = find_dates(event)
    now = datetime.datetime.now()
    if (start_dt-now).days < 7 and end_dt > now:
        return True
    return False

def job():
    global df
    results = get_data_from_API()
    for event in results:
        if check_event(event) and (event['id'] not in list(df['id'])):
            print('Найдено подходящее событие:', event['title'])
            _, _, start_txt, end_txt = find_dates(event)
            print('Событие продлится с {} по {}.'.format(start_txt, end_txt))
            print('Подробности - здесь:', event['site_url'])
            df = df.append(fill_df(event), ignore_index = True)

def make_summary():
    df.to_excel('events.xlsx', index = False)
    print('Новая копия файла events.xlsx создана в', datetime.datetime.now().strftime('%H:%M:%S'))

df = pd.DataFrame(columns = 'id title description price start_date end_date url'.split())

job()
make_summary()
