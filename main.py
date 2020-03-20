#-- coding: utf8 --
#!/usr/bin/env python3

import os
import sys
import json
import argparse
import fake_useragent

from director import Director

from termcolor import colored

def CreateArgument():
    arg = argparse.ArgumentParser()
    arg.add_argument('name', nargs='?')
    return arg

def CreateJSONFile(title, quote, author, text):
  
    data = {
        "title": str(title),
        "quote": str(quote),
        "author": str(author),
        "article_text": str(text),
    }    

    with open("data_file.json", "w") as outfile:
        json.dump(data, outfile, indent=2)

if __name__ == "__main__":
    os.system('clear')
    argument = CreateArgument()
    article_url = argument.parse_args().name

    article = Director(article_url)
    # Получение заголовка/цитаты/автора/статьи
    title, quote, author, article_text = article.create_article()    

    # Создание JSON файла
    CreateJSONFile(title, quote, author, article_text)
    print(article_text)

    print("All done!")
    


    


    
    