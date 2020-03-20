#-- coding: utf8 --
#!/usr/bin/env python3

from html_builder import HtmlParser
from article_builder import ArticleParser


class Director():
    def __init__(self, url):
        self.url = url

        self.regex_dict = {
            r'<\/div>|<div.*?>': '',
            r'class=\".+?\"|id=\".*?\"': '',            
            r'<p.*?>': '<p class="text">',
            r'<ul.*?>': '<ul class="text">',
            r'<ol.*?>': '<ol class="text">',
            r'<h3.*?>': '<h3 class="text">',

        }

        self.replace_dict = {
            'strong>': 'b>',
            '</p>': '</p>\n\n',
            '</ul>': '</ul>\n',
            '</ol>': '</ol>\n',
            '</h3>': '</ol>\n',
        }
    
    def create_article(self):
        """Создание статьи в нужном формате"""

        article_html = HtmlParser(self.url)             
        article = article_html.get_content(article_html.get_html(self.url))

        title = article.h1.get_text() # Получение заголовка     
        
        article = ArticleParser(article)

        quote = article.tag_text('blockquote', class_='article_decoration_first')
        author = article.tag_text('blockquote', class_='article_decoration_last')
              
        # Предварительная очистка
        article_text = article.simple_replacement_cleaning()

        # Цикл замены совпадений через регулярные выражения
        for regex in self.regex_dict:
            article_text = article.re_replacement_cleaning(regex, self.regex_dict[regex])

        # Цикл простой замены по совпадениям
        for r in self.replace_dict:
            article_text = article_text.replace(r, self.replace_dict[r])  

        # Проверка, есть ли автор цитаты
        if quote != author:
            return (title, quote, author, article_text)

        elif quote == author:
            author = ''
            return (title, quote, author, article_text)
        
        else:
            print("Произошла ошибка при получении данных, повторите попытку...")
        


