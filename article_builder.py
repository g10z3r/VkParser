#-- coding: utf8 --
#!/usr/bin/env python3

import re

# Пошаговое приведение статьи к нужному виду разными строителями
class ArticleParser():
    """Класс предназаначен для обрабтки <div> контента"""
    def __init__(self, article):
        self.article = article  
        
    def re_replacement_cleaning(self, regex, regex_key):
        # Основной строитель
        """Замена фрагмента найденного регулярным выражением"""
        for _ in re.findall(regex, str(self.article)):
            self.article = str(self.article).replace(_, regex_key)
        
        return self.article

    def tag_text(self, tag, class_):
        """Получение текста без HTML разметки из
        определенного тега (при условии что он существует)"""

        return (self.article.find(tag, class_).get_text() 
                if self.article.find(tag, class_) in self.article 
                else '')