import calendar
import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from datetime import datetime, date
from lxml import html
import requests

# Open URL

page = requests.get('https://rijkswaterstaatverkeersinformatie.nl/VI/overzicht')
tree = html.fromstring(page.content)

col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []

# Scrape data and append to lists

for x in tree.xpath("//dl[@itemscope='itemscope']"):

    col1.append(datetime.now().date())
    col2.append(datetime.now().strftime('%H:%M'))
    col3.append(calendar.day_name[date.today().weekday()])
    col4.append('1')

    try:
        road = x.xpath(".//span[@class='vi-wegnr']/text()")
        col5.append(road[0])
    except:
        col5.append(np.nan)

    if x.xpath(".//dt[@class='vi-hoofdtraject vi-bericht']"):
        location_1 = x.xpath(".//dt[@class='vi-hoofdtraject vi-bericht']/text()")
        col6.append(location_1[0])
        col7.append("Traffic_Jam")
    elif x.xpath(".//dt[@class='vi-hoofdtraject vi-langdurig']"):
        location_1 = x.xpath(".//dt[@class='vi-hoofdtraject vi-langdurig']/text()")
        col6.append(location_1[0])
        col7.append("Permanent_Construction")
    else:
        col6.append(np.nan)
        col7.append("NA")

    if x.xpath(".//dd[@class='vi-traject vi-bericht']"):
        location_2 = x.xpath(".//dd[@class='vi-traject vi-bericht']/text()")
        col8.append(location_2[0])
    elif x.xpath(".//dd[@class='vi-traject vi-langdurig']"):
        location_2 = x.xpath(".//dd[@class='vi-traject vi-langdurig']/text()")
        col8.append(location_2[0])
    else:
        col8.append("NA")

    if x.xpath(".//span[@class='italic']"):
        description = x.xpath(".//span/text()")
        u = description[2:]
        col9.append(u)
    elif x.xpath(".//span"):
        description = x.xpath(".//span/text()")
        description_clean = description[5:]
        col9.append(description_clean)
    else:
        col9.append("NA")

    if x.xpath(".//span[@itemprop='value']"):
        km = x.xpath(".//span[@itemprop='value']/text()")
        col10.append(km[0])
    else:
        col10.append("NA")

# append to DataFrame and clean up

df = pd.DataFrame({'date': col1, 'time': col2, 'day': col3,'bin': col4, 'road': col5, 'location_1': col6, 'type': col7, 'location_2': col8, 'description': col9 , 'km': col10})
df.fillna(method='ffill', inplace=True)
df.set_index('date', inplace=True)
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True, ascending=True)
print(df.to_string())

# Optional - SQL connection

engine = create_engine('enter_postgres_link_here')
df.to_sql('enter_name_of_sql_database', engine, if_exists='append')

