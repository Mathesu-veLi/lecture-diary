import sys
from module import Diary


def main():
    """
    Usage: lecture_diary [OPTION]

    OPTIONS:
        -a, --add <title> <author> <start_date> <end_date>  Add a new book to the diary
        -e, --edit <index> [EDIT OPTIONS]                   Edit the existing book
        -r, --read                                          Read the diary
        -h, --help                                          Show this message and exit
    
    EDIT OPTIONS:
        -t, --title <title>             Edit title
        -a, --author <author>           Edit author
        -sd, --start_date <start_date>  Edit start date
        -ed, --end_date <end_date>      Edit end date
    """
    
    try:
        diary = Diary()
        
        if len(sys.argv) > 6: raise IndexError()
        
        match sys.argv[1]:
            case '-r' | '--read':
                if not len(diary.read().index):
                    return print('Diary is empty...')
                
                print(diary.read())
                
            case '-a' | '--add':
                if len(sys.argv) < 6: 
                    raise IndexError()

                diary.add(sys.argv[2:])
                
            case '-e' | '--edit':
                if len(sys.argv) < 5: 
                    raise IndexError()

                diary.edit(sys.argv[2], sys.argv[3], sys.argv[4])
                
            case '-h' | '--help':
                help(main)
                
            case _:
                print(sys.argv[1] + ' is not a valid option')
                
    except IndexError:
        print("Incorrect usage!")
        print("Usage: lecture_diary [OPTION]")
        print('(-h to help)')
        
    except FileNotFoundError:
        print("File diary.csv not found")
        creates = True if input('Creates a diary? [Y/N]: ').capitalize()[0] == 'Y' else False
        
        if creates:
            diary = Diary()
            diary.create()
    
    
if __name__ == '__main__':
    main()