#-- coding: utf8 --
#!/usr/bin/env python3

import urllib.request
import requests, fake_useragent

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Строители первоночального вида статьи
class HtmlParser():
    """Класс получает html разметку страницы и выделяет <div> контента"""
    def __init__(self, url):
        self.url = url

        self.session = requests.Session()
        self.user_agent = fake_useragent.UserAgent()
        self.user = str(self.user_agent.random)
        self.headers = {
            'User-Agent':f'{self.user}',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language':'en-US',
        }

    def get_html(self, url):
        # Первый строитель
        """Получает контент страницы"""                      
        page = requests.get(str(url.split()[0]), headers = self.headers)
        bsObj = BeautifulSoup(page.text, 'lxml')
        return bsObj

    def get_content(self, bsObj, class_name = 'article article_view'):
        # Второй строитель
        """Получает непосредственно <div> контента"""
        article_text_html = bsObj.find('div', class_= class_name)
        return article_text_html
