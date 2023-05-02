#!/usr/bin/env python3

class Book:
    def __init__(self, title = 'And Then There Were None', author = 'Agatha Christie', page_count = 0):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_page_count(self):
        return self._page_count
    
    def set_title(self, title):
        if (type(title) == str) and (1 <= len(title)):
            self._title = title
        return 
    
    def set_author(self, author):
        if (type(author) == str) and (1 <= len(author)):
            self._author = author
        else:
            pass

    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
        else:
            print('page_count must be an integer')
        return
    
    def turn_page(self):
        self._page_count += 1
        print('Flipping the page...wow, you read fast!')
    
    title = property(get_title, set_title)
    author = property(get_author, set_author)
    page_count = property(get_page_count, set_page_count)
