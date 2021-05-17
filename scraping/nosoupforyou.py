#!/usr/bin/python3
"""
Using BeautifulSoup to make data selections from montypython.html
"""

from bs4 import BeautifulSoup

# retrieve the raw HTML using the open function then read in the data
raw_html = open('http://florgeous.com/types-of-flowers/').read()
# use the backend parser 'html.parser' to parse out the raw_html
html = BeautifulSoup(raw_html, 'html.parser')

# the select method on the html object allows the selection of
# CSS selectors to locate elements in the document
# return a list of paragraph elements (dict like)
for h3 in html.select('h3'):
    print(h3.text)
    #if p['id'] == 'camelot' or p['id'] == 'knights':
     #   print(p.text)

