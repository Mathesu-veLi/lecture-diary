import pandas as pd
import sys

def add():
    new_book = {
        'name': [sys.argv[2]],
        'author': [sys.argv[3]],
        'start_date': [sys.argv[4]],
        'end_date': [sys.argv[5]]
    }
    #TODO: Validate start_date and end_date
    new_book = pd.DataFrame(new_book)
    
    try:
        df = pd.read_csv('diary.csv')
        df = pd.concat([df, new_book])
    except FileNotFoundError:
        df = new_book
    finally:
        df.to_csv('diary.csv', index=False)
    
def read():
    df = pd.read_csv('diary.csv')
    return df
    
#TODO: Add a import of diary's