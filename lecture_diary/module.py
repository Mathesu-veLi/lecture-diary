import pandas as pd
    
#TODO: Add a import of diary's

class Book:
    def __init__(self, book_data):
        self.title = book_data[0]
        self.author = book_data[1]
        self.start_date = book_data[2]
        self.end_date = book_data[3]
        
    def __str__(self):
        book_obj = {
            'title': self.title,
            'author': self.author,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
        
        return book_obj

class Diary:
    def __init__(self):
        self.df = None
        
    def read(self):
        if self.df is None:
            try:
                self.df = pd.read_csv('diary.csv')
            except pd.errors.EmptyDataError:
                print('No data in diary.csv')
                
        return self.df
            
    
    def create(self) -> None:
        pd.DataFrame().to_csv('diary.csv', index=False)
    
    def add(self, new_book: Book):
        new_book_df = pd.DataFrame(new_book)
    
        try:
            df = pd.concat([self.df, new_book_df])
        except FileNotFoundError:
            df = new_book_df
        finally:
            df.to_csv('diary.csv', index=False)
            