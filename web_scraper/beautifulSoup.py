from bs4 import BeautifulSoup

# opening file in read mode 
with open("dummy_html.html", "r") as file: 
    doc = BeautifulSoup(file, "html.parser")

def find_title(document): 
    title = doc.title
    return title 

title = find_title(doc)

# turns doc title into a list 
def title_listy(title): 
   listy = [] 
   for word in title: 
       listy.append(word)
   return listy 

# turns doc title into a string
def title_to_str(title): 
    stringy = "" 
    for word in title: 
        stringy += word 
    return stringy 

# turns doc title into a string with default title attribute 
title_text = doc.title.text

