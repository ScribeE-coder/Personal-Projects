from bs4 import BeautifulSoup

# opening file in read mode 
with open("dummy_html.html", "r") as file: 
    doc = BeautifulSoup(file, "html.parser")

title = doc.title
print(title)
