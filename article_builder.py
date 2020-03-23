#-- coding: utf8 --
#!/usr/bin/env python3

import re

# Пошаговое приведение статьи к нужному виду разными строителями
class ArticleParser():
    """Класс предназаначен для обрабтки <div> контента"""
    def __init__(self, article):
        self.article = article
        
        self.tag_list = ['h1', 'blockquote']
        
    def re_replacement_cleaning(self, regex, regex_key):
        # Основной строитель
        """Замена фрагмента найденного регулярным выражением"""
        for _ in re.findall(regex, str(self.article)):
            self.article = str(self.article).replace(_, regex_key)
        
        return self.article

    def tag_text(self, tag, class_):
        """Получение текста без HTML разметки из
        определенного тега (если он существует)"""
        if self.article.find(tag, class_) in self.article:
            tag_text = self.article.find(tag, class_).get_text()
        else:
            tag_text = ''

        return tag_text