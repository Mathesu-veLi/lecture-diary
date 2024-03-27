import pandas as pd
    
#TODO: Add a import of diary's

class Book:
    def __init__(self, name, author, start_date, end_date):
        self.name = name
        self.author = author
        self.start_date = start_date
        self.end_date = end_date
        
    def __str__(self):
        book_obj = {
            'name': self.name,
            'author': self.author,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
        
        return book_obj

class Diary:
    def __init__(self):
        self.df = pd.read_csv('diary.csv')
        
    def read(self):
        return self.df
    
    def add(self, new_book: Book):
        new_book_df = pd.DataFrame(new_book)
    
        try:
            df = pd.concat([self.df, new_book_df])
        except FileNotFoundError:
            df = new_book_df
        finally:
            df.to_csv('diary.csv', index=False)
            