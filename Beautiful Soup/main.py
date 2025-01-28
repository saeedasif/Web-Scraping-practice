#  Practice of Beautiful soup

import requests
from bs4 import BeautifulSoup

with open("sample.html",'r') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')


# print(soup.prettify()) # GIVE ALL THE HTML CODE IN THE FILE and format it

# print(soup.title)  # just gives tag the title  

# print(soup.title.prettify(),     type(soup))  

# print(soup.title.string,     type(soup.title.string)) #give the inner context of title

# print(soup.title.name,     type(soup.title.string))# gives the the element or tag name like title

# print(soup.title.parent.name) # gives the parent of title

# print(soup.p.string) # find  the first p tag in file

# print((soup.findAll("p"))) # give the list of all the p in the file

# print(soup.p['class']) #gives the first  p  element class name

# print(soup.find(id = "ali").text)# it give the text inside the ali i

# print(soup.get_text())  # Get all the text in the html file
# link =  soup.a

# print (link.get_text()) # Give the text inside the a tag
# link1 = soup.find_all('a')[1]
# print(f"2nd Link {link1['href']}")
# for idx,link in enumerate(soup.find_all('a'), start=1):
#     print(f"links {idx} :  {link.get('href')}")

# print(soup.select("div.italic"))  #get all the  div with class italic 
# id = soup.select("div#saeed")

# print(f"id inner context = {id[0].text}") # get the inner context of div with id saeed 



# for child in soup.find(class_='cont').children: # Find all the child of a tag and also the same parent would also be finded
#     print(child)
 
# cont = soup.find(class_= "cont")  # Changing the tag and their class and inner context
# print(cont)
# cont.name = "span"
# print(cont)
# cont['class'] = 'container'
# print(cont)
# cont.string = 'Saeed'
# print(cont)


# ulTag = soup.new_tag("ul")  # create and  insert the new tag into html and from a new file and write into it

# liTag = soup.new_tag("li")
# liTag.string = 'Home'
# ulTag.append(liTag)


# liTag = soup.new_tag("li")
# liTag.string = 'About'
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)


# with open("modified.html",'w') as f:
#     f.write(str(soup))




