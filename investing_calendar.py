import requests
from bs4 import BeautifulSoup

# Change the lang, timeZone, calType as you like.
# calType : day, week
# If you want english version, change the lang to 1.
# ex) &lang=18 ->> &lang=1
uri = 'https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,' \
      'exc_previous&features=datepicker,timezone&countries=110,43,17,42,5,178,32,12,26,36,4,72,10,14,48,35,37,6,122,' \
      '41,22,11,25,39&calType=day&timeZone=88&lang=18'


class InvestingCalendar:
    def __init__(self):
        self.uri = uri
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/41.0.2227.0 Safari/537.36'
        }
        self.req = requests.get(self.uri, headers=self.header)
        self.news = []

    def get_news(self):
        html = self.req.text

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {"id": "ecEventsTable"})
        tbody = table.find('tbody')
        rows = tbody.findAll('tr')

        for tr in rows:
            news_info = {'time': None,
                         'country': None,
                         'impact': None,
                         'event_title': None,
                         'bold': None,
                         'fore': None,
                         'prev': None,
                         'signal': None,
                         'type': None}

            time = tr.find('td', {'class': 'time'})
            if not time:
                continue

            news_info['time'] = time.get_text()

            cols = tr.find('td', {"class": "flagCur"})
            flag = cols.find('span', {'class': 'ceFlags'})
            news_info['country'] = flag.get("title")

            impact = tr.find('td', {"class": "sentiment"})
            bulls = impact.findAll('i', {"class": "grayFullBullishIcon"})
            news_info['impact'] = len(bulls)

            event = tr.find('td', {"class": "event"})
            news_info['event_title'] = event.text.strip()
            news_type = event.find('span')
            if news_type:
                news_info['type'] = news_type.get("title")

            bold = tr.find('td', {'class': 'bold'})
            if bold:
                news_info['bold'] = bold.text.strip()
                news_info['signal'] = bold.get("title")

            fore = tr.find('td', {'class': 'fore'})
            if fore:
                news_info['fore'] = fore.text.strip()

            prev = tr.find('td', {'class': 'prev'})
            if prev:
                news_info['prev'] = prev.text.strip()

            self.news.append(news_info)

        return self.news


if __name__ == '__main__':
    investing_calendar = InvestingCalendar()
    print(investing_calendar.get_news())

