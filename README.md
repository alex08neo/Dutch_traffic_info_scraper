# Python-based webscraper for scraping traffic data from the Dutch traffic information service, [vid.nl](https://www.vid.nl)

### Webscraper written in Python, which with the help of [Selenium](https://pypi.python.org/pypi/selenium), scrapes traffic data from the Dutch main traffic service platform, [vid.nl](https://www.vid.nl). Headline variables retrieved are the highway or expressway under consideration, the location of the traffic jam, the reason for the traffic jam, the date, time and day of the week.

This scraper has initially been created to compile a vast database of traffic info / jams in the Netherlands. For this reason, this script has an " initial" and " subsequent" loop. The " initial" script creates a DataFrame, which gets saved / exported as a CSV. This CSV in turn can be appended to in "subsequent" runs. Kindly note, one would have to manually switch between the " initial" and " subsequent" runs.

This tool has been written by means of:

 - [Python 3.6.5](https://www.python.org/downloads/release/python-365/)
 - [Selenium 3.12](https://docs.seleniumhq.org/download/)
 - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

Please note:

- you will have to point the browser variable to the local path of your webdriver

Example of the resulting dataframe:

```

date             additional bin     day                        location-1

2018-06-17               NA   1  Sunday             A27Gorinchem - Almere
2018-06-17               NA   1  Sunday                N33Veendam - Assen
2018-06-17               NA   1  Sunday     N59Zierikzee - Hellegatsplein
2018-06-17               NA   1  Sunday                  A59Zonzeel - Oss
2018-06-17               NA   1  Sunday     N59Hellegatsplein - Zierikzee
2018-06-17  een brugopening   1  Sunday         N196Hoofddorp <> Uithoorn
2018-06-17  een brugopening   1  Sunday  N207Alphen aan den Rijn <> Lisse
2018-06-17       vertraging   1  Sunday          N302Enkhuizen - Lelystad
2018-06-17  een brugopening   1  Sunday           N514Krommenie <> Wormer

location-2                                          road  time
                                               NA   A27  13:13
                                               NA   N33  13:13
                                               NA   N59  13:13
                                               NA   A59  13:13
                                               NA   N59  13:13
in beide richtingen ter hoogte van de Aalsmeer...  N196  13:13
in beide richtingen ter hoogte van de Elsbroek...  N207  13:13
    tussen Naviduct Krabbersgat en de Houtribbrug  N302  13:13
in beide richtingen ter hoogte van de Prins Cl...  N514  13:13

```
