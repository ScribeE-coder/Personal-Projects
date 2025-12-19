from bs4 import BeautifulSoup

class Web_Scraper: 
    def __init__(self, file): 
        self.file = file
        # opening file in read mode (defaults to read "r" not necessary) 
        with open(self.file) as read_file: 
            self.doc = BeautifulSoup(read_file, "html.parser") 

    def find_title(self): 
        self.title = self.doc.title 
        return self.title 
    
    #mutates title and returns in string format 
    def modify_title(self, new_title):
        self.title.string = str(new_title)
        self.title = self.doc.title.text
        return self.title
    
    # turn doc title into a list 
    def title_to_list(self):
        listy = [] 
        for word in self.title: 
            listy.append(word)
        return listy 
    
    # converts title to string 
    def title_to_string(self): 
        self.title = self.title.text
        return self.title 
    
    # find first instance of given tag 
    def find_tag(self, tag): 
        tag = self.doc.find(tag) 
        return tag 
    
    # find all instances of given tag 
    def find_all_tags(self, tag): 
        tags = self.doc.find_all(tag)
        return tags 

web_scrape = Web_Scraper("dummy_html.html")
title = web_scrape.find_title()



