#  Practice of Beautiful soup

import requests
from bs4 import BeautifulSoup

with open("sample.html",'r') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify()) # GIVE ALL THE HTML CODE IN THE FILE
print(soup.title)  # just format it better
print(soup.title.prettify(),     type(soup))  
print(soup.title.string,     type(soup.title.string))
print(soup.title.name,     type(soup.title.string))# gives the the element or tag name like title
print(soup.title.parent.name) # gives the parent of title
print(soup.p.string) # find  the first p tag in file
print((soup.findAll("p"))) # give the list of all the p in the file
print(soup.p['class']) #gives the first p  element class name
print(soup.find(id = "ali").text)# it give the text inside the ali i

print(soup.get_text())  # Get all the text in the html file
link =  soup.a
print (link.get_text()) # Give the text inside the a tag
link1 = soup.find_all('a')[1]
print(f"2nd Link {link1['href']}")
for idx,link in enumerate(soup.find_all('a'), start=1):
    print(f"links {idx} :  {link.get('href')}")
print(soup.select("div.italic"))  #get all the  div with class italic 
id = soup.select("div#saeed")
print(f"id inner context = {id[0].text}") # get the inner context of div with id saeed 


