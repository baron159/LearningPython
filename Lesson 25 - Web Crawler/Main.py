__author__ = 'Scott'

import requests as req
from bs4 import BeautifulSoup as soup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:

