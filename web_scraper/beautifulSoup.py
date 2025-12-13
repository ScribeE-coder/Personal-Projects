from bs4 import BeautifulSoup

# opening file in read mode 
with open("dummy_html.html", "r") as file: 
    doc = BeautifulSoup(file, "html.parser")


def find_title(document): 
    title = doc.title
    return title 

title = find_title(doc)

def title_listy(title): 
    words = []
    for word in title: 
        words.append(word)
    return words

def title_to_str(words): 
    stringy = "" 
    for word in words: 
        stringy += word 
    return stringy 

word_listy = title_listy(title)
stringy_title = title_to_str(word_listy)
print(stringy_title) 

