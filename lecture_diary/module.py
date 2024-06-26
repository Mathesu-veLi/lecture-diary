import pandas as pd
import os, re, datetime
    
#TODO: Add a import of diary's

class Book:
    def __init__(self, book_data):
        self.title = book_data[0]
        self.author = book_data[1]
        self.start_date = self.date_is_valid(book_data[2])
        self.end_date = self.date_is_valid(book_data[3])
        
    def to_dict(self):
        book_obj = {
            'title': [self.title],
            'author': [self.author],
            'start_date': [self.start_date],
            'end_date': [self.end_date]
        }
        
        return book_obj
    
    def date_is_valid(self, date):
        pattern = r'(\d{4})-(\d{2})-(\d{2})'
        match = re.search(pattern, date)

        if not match:
            return False
        
        try:
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            datetime.datetime(year, month, day)
            return date
        except ValueError:
            return False
        

class Diary:
    def __init__(self):
        self.df = None
        
    def read(self) -> pd.DataFrame:
        if self.df is None:
            self.df = pd.read_csv('diary.csv')
            
        return self.df
        
        
    def create(self) -> None:
        df = pd.DataFrame(columns=['title', 'author', 'start_date', 'end_date'])
        df.to_csv('diary.csv', index=False)
        
    
    def add(self, new_book: Book):
        new_book = Book(new_book)
        if not new_book.start_date or not new_book.end_date:
            print('Invalid date. Hint: Use YYYY-MM-DD')
            return
        
        df = pd.DataFrame(new_book.to_dict())
        
        file_exists = os.path.exists('diary.csv')
        if not file_exists:
            raise FileNotFoundError()   
        
        df.to_csv('diary.csv', mode='a', header=False, index=False)
        
        print('Book added')
    
    def edit(self, book_index: int, column_to_edit: str, new_book_data: str):
        if column_to_edit not in ['title', 'author', 'start_date', 'end_date']:
            print('Invalid column to edit. Hint: Use title, author, start_date, or end_date')
            return
        
        if column_to_edit in ['start_date', 'end_date']:
            new_book_data = Book().date_is_valid(self, new_book_data)
            if not new_book_data:
                print('Invalid date. Hint: Use YYYY-MM-DD')
                return
        
        df = pd.read_csv('diary.csv')
        df.at[int(book_index), column_to_edit] = new_book_data
        df.to_csv('diary.csv', index=False)
        
        print('Book edited')