import sys
from module import read, add


def main():
    """
    Usage: lecture_diary [OPTION]

    OPTIONS:
        -a, --add <name> <author> <start_date> <end_date>   Add a new book to the diary
        -h, --help                                          Show this message and exit
        -r, --read                                          Read the diary
    """
    
    try:
        match sys.argv[1]:
            case '-r' | '--read':
                print(read())
            case '-a' | '--add':
                add()
            case '-h' | '--help':
                help(main)
            case _:
                print(sys.argv[1] + 'is not a valid option')
    except IndexError:
        print("Usage: lecture_diary [OPTION]")
        print('(-h to help)')
    
    
if __name__ == '__main__':
    main()