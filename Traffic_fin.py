
import calendar
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime, date
import time
from random import randint

# Define browser

browser = webdriver.Chrome('/Users/Mike/Downloads/chromedriver')
browser.get('https://rijkswaterstaatverkeersinformatie.nl/VI/overzicht')
time.sleep(randint(1, 5))


col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []

# Retrieve data

for item in browser.find_elements_by_xpath("//dl[@itemscope='itemscope']"):
        col1.append(datetime.now().date())
        col6.append('1')
        col7.append(datetime.now().strftime('%H:%M'))
        col8.append(calendar.day_name[date.today().weekday()])

for item in browser.find_elements_by_xpath("//dl[@itemscope='itemscope']"):
    try:
        road = item.find_element_by_css_selector("span.vi-wegnr").text
        col2.append(road)

    except(TimeoutException, NoSuchElementException):
        col2.append(np.nan)

for item in browser.find_elements_by_xpath("//dl[@itemscope='itemscope']"):
    try:
        location_1 = item.find_element_by_css_selector("dt.vi-hoofdtraject.vi-bericht").text
        col3.append(location_1)
    except(TimeoutException, NoSuchElementException):
        try:
            u = item.find_element_by_css_selector("dt.vi-hoofdtraject.vi-langdurig").text
            col3.append(u)
        except(TimeoutException, NoSuchElementException):
            col3.append("NA")

for item in browser.find_elements_by_xpath("//dl[@itemscope='itemscope']"):
    try:
        location_2 = item.find_element_by_css_selector("dd.vi-traject.vi-bericht").text
        col4.append(location_2)

    except(TimeoutException, NoSuchElementException):
        col4.append("NA")

for item in browser.find_elements_by_xpath("//dl[@itemscope='itemscope']"):
    try:
        message = item.find_element_by_css_selector("dd.vi-bericht.italic").text
        col5.append(message)

    except(TimeoutException, NoSuchElementException):
        col5.append("NA")

# Append data to Dataframe

df = pd.DataFrame({'date': col1, 'road': col2, 'location-1': col3,'location-2': col4, 'additional': col5, 'bin': col6, 'time': col7, 'day': col8})
df.fillna(method='ffill', inplace=True)
df.set_index('date', inplace=True)
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True, ascending=True)

# Initial run - save data to CSV

print(df.to_string())
df.to_csv("data.csv", sep=';', encoding='utf-8')

# Subsequent runs - append data to existing CSV

df_existing = pd.read_csv('data.csv', sep=';')
df_existing.set_index('date', inplace=True)
df_existing.index = pd.to_datetime(df_existing.index)
df_existing.sort_index(inplace=True, ascending=True)

df_new = df_existing.append(df)

print(df_new.to_string())
df_new.to_csv("data.csv", sep=';', encoding='utf-8')
