import requests
from bs4 import BeautifulSoup
class Input:

    def getInputSearchText(self):
        # print('1. get user\'s input search text')
        return 'python convert list to'

    def doCrawlingByText(self, searchText):
        # print('2. crawling google searched result with search text' + ': ' + searchText)
        url = 'https://www.google.co.kr/search?q='+searchText+'sourceid=chrome&ie=UTF-8/'
        plain_text = requests.get(url).text
        soup = BeautifulSoup(plain_text, 'lxml')
        crawled = {}
        for link in soup.select('h3 > a'):
            crawled[link.text] = link.get('href')
        return crawled


