#  Practice of Beautiful soup

import requests
from bs4 import BeautifulSoup

with open("sample.html",'r') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.prettify(),     type(soup))
# print(soup.title.string,     type(soup.title.string))
# print(soup.title.name,     type(soup.title.string))# gives the the element or tag of title
# print(soup.title.parent.name) # gives the parent of title
# print(soup.p.string) # find  the first p tag in file
# print((soup.findAll("p"))) # give the list of all the p in the file

# print(soup.find(id = "ali").text)# it give the class of the element


