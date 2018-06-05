from bs4 import BeautifulSoup
import urllib
import requests
import sys
import random

def get():
    titre = []
    url = 'http://intertitre.togdazine.ru'
    with urllib.request.urlopen(url) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        img = soup.find_all('img','w-article-all-item__image', limit = 6)
        for n in img:
            m = url + n.get('src')
            titre.append(m)
    return (titre)
    




