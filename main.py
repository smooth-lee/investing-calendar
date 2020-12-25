import requests
from bs4 import BeautifulSoup

uri = 'https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=110,43,17,42,5,178,32,12,26,36,4,72,10,14,48,35,37,6,122,41,22,11,25,39&calType=day&timeZone=88&lang=18'


class InvestingCalendar:
    def __init__(self):
        self.uri = uri
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'
        }
        self.req = requests.get(self.uri, headers=self.header)
        self.news = []

    def get_news(self):

        html = self.req.text

        soup = BeautifulSoup(html, 'html.parser')

        print(soup)


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    news = InvestingCalendar()
    news.get_calendar_info()

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 확인
