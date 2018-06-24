# Python-based webscraper for scraping traffic data from the Dutch traffic information service, [vid.nl](https://www.vid.nl)

### Webscraper (for local-usage) written in Python, which with the help of [Selenium](https://pypi.python.org/pypi/selenium), scrapes traffic data from the Dutch main traffic service platform, [vid.nl](https://www.vid.nl). Headline variables retrieved are the highway or expressway under consideration, the location of the traffic jam, the reason for the traffic jam, the date, time and day of the week.

This scraper has initially been created to compile a vast database of traffic info / jams in the Netherlands. For this reason, this script has an " initial" and " subsequent" loop. The " initial" script creates a DataFrame, which gets saved / exported as a CSV. This CSV in turn can be appended to in "subsequent" runs. Kindly note, one would have to manually switch between the " initial" and " subsequent" runs.

This script has been written by means of:

 - [Python 3.6.5](https://www.python.org/downloads/release/python-365/)
 - [Selenium 3.12](https://docs.seleniumhq.org/download/)
 - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

Please note:

- you will have to point the browser variable to the local path of your webdriver

#### NB - in the "lxml" folder you will find a light-weight version of the scraper (not dependent on ChromeDriver or Selenium). This version is ideal for deployment on cloud application platform's like [Heroku](https://www.heroku.com). I've added the corresponding Procfile and requirements.txt should you wish to deploy this scraper on the latter platform. This version also includes an SQL-hook for interaction with a PostgreSQL-database.

Example of the resulting dataframe:

```

date             additional bin     day                        location-1

2018-06-17               NA   1  Sunday                Gorinchem - Almere
2018-06-17               NA   1  Sunday                   Veendam - Assen
2018-06-17               NA   1  Sunday        Zierikzee - Hellegatsplein
2018-06-17               NA   1  Sunday                     Zonzeel - Oss
2018-06-17               NA   1  Sunday        Hellegatsplein - Zierikzee
2018-06-17  een brugopening   1  Sunday             Hoofddorp <> Uithoorn
2018-06-17  een brugopening   1  Sunday      Alphen aan den Rijn <> Lisse
2018-06-17       vertraging   1  Sunday              Enkhuizen - Lelystad
2018-06-17  een brugopening   1  Sunday               Krommenie <> Wormer

location-2                                          road  time type
                                               NA   A27  13:13 Permanent_Construction
                                               NA   N33  13:13 Traffic_Jam
                                               NA   N59  13:13 Traffic_Jam
                                               NA   A59  13:13 Traffic_Jam
                                               NA   N59  13:13 Traffic_Jam
in beide richtingen ter hoogte van de Aalsmeer...  N196  13:13 Permanent_Construction
in beide richtingen ter hoogte van de Elsbroek...  N207  13:13 Permanent_Construction
    tussen Naviduct Krabbersgat en de Houtribbrug  N302  13:13 Permanent_Construction
in beide richtingen ter hoogte van de Prins Cl...  N514  13:13 Permanent_Construction

description                                         km

[afgesloten verbindingsweg naar de A10 richtin...   NA
wegafsluiting\n      in verband met\n      , ...    3
wegafsluiting\n      in verband met\n      , ...    2
wegafsluiting\n      in verband met\n      , ...    NA
[een brugopening]                                   NA
[een brugopening]                                   NA
[afgesloten verbindingsweg naar de A4 richtin...    NA
wegafsluiting\n      in verband met\n      , ...    1
wegafsluiting\n      in verband met\n      , ...    2

```
