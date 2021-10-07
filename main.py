import requests
from bs4 import BeautifulSoup

url = 'https://blog.mozilla.org/en/category/mozilla/news/'

headers = {'user agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
           }

respons = requests.get(url, headers=headers)
# print(respons)
soup = BeautifulSoup(respons.text, 'html.parser')

news = soup.findAll('section', class_='mzp-c-card mzp-has-aspect-1-1')
# print(news)

for title in news:
    title = title.find('h2', class_='mzp-c-card-title')
    print(title.text)