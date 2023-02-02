#T67 Grant Phillips 
import string
from T67_P3_sorting_fun import sort_books_title
from T67_P3_sorting_fun import sort_books_author
from T67_P3_sorting_fun import sort_books_ascending_rate
from T67_P3_sorting_fun import sort_books_publisher
from T67_P2_add_remove_search_dataset import get_books_by_rate
from T67_P2_add_remove_search_dataset import get_the_books_by_category
from T67_P2_add_remove_search_dataset import get_publisher_books
from T67_P2_add_remove_search_dataset import get_books_by_title
from T67_P2_add_remove_search_dataset import get_books_by_author
from T67_P2_add_remove_search_dataset import get_all_categories_for_book_title
from T67_P2_add_remove_search_dataset import add_book
from T67_P2_add_remove_search_dataset import remove_book
from T67_P5_load_data import book_category_dictionary

command_list = ['L','A','R','G','GCT','S','Q']

def main_menu():
    '''Prints out the main menu of the user interface
    main_menu()
    >>>1- L)oad data
       2- A)dd book
       3- R)emove book
       4- G)et books
          T)itle   R)ate   A)uthor   P)ublisher   C)ategory
       5- GCT) Get all Categories for book Title
       6- S)ort books
          T)itle   R)ate   P)ublisher   A)uthor
       7- Q)uit
    '''
    print("The available commmands are:\n1- L)oad data\n2- A)dd book\n3- R)emove book\n4- G)et books\n   T)itle   R)ate   A)uthor   P)ublisher   C)ategory\n5- GCT) Get all Categories for book Title\n6- S)ort books\n   T)itle   R)ate   P)ublisher   A)uthor\n7- Q)uit\n")
    
def prompt_for_command()-> str:
    '''Prompts user to enter a command
    promt_for_command()
    >>> Please type your command: 
    '''
    first1 = input('Please type your command: ')
    first = first1.upper()
    print('You entered,',first.upper(),'\n')    
    return first
def commands(first:str)-> None:
    global x
    global a
    global dictionary
    if first == 'L':
        print('What file would you like to be loaded?\n')
        file = input()
        dictionary = book_category_dictionary(str(file))
        if dictionary != 0:
            print('The file has been loaded\n')
            a = 1
    if first == 'Q':
        print('Goodbye')
        x = 1
        a = 1
    if first not in command_list and a ==0:
        print(first," is not a command.\n")
    elif a == 0:
        print("The file has not been loaded\n")
    else:
        if first == 'S':
            if dictionary != 0:
                print('How do you want to sort?\n')
                print('Sort by: T)itle R)ate P)ublisher A)uthor\n')
                seccond = input()
                seccond2 = seccond.upper()
                if seccond2 == 'T':
                    print('Sorting by: Title\n')
                    print(sort_books_title(dictionary),'\n')
                if seccond2 == 'R':
                    print('Sorting by: Rate\n')
                    print(sort_books_ascending_rate(dictionary),'\n')
                if seccond2 == 'P':
                    print('Sorting by: Publisher\n')
                    print(sort_books_publisher(dictionary),'\n')
                if seccond2 == 'A':
                    print('Sorting by: Author\n')
                    print(sort_books_author(dictionary),'\n')
            else:
                print('File not loaded\n')  
        if first == 'G':
            Get_Books = input('How do you want to get books?\nT)itle, R)ate, A)uthor, P)ublisher, or C)ategory: \n')
            if Get_Books.upper() == 'R':
                rate = input('Enter a Rate: \n')
                print(get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), int(rate)))
            elif Get_Books.upper() == 'A':
                author_name = input('Enter an Author: \n')
                print(get_books_by_author(book_category_dictionary('google_books_dataset.csv'), author_name))
            elif Get_Books.upper() == 'T':
                title = input('Enter a Title: \n')
                print(get_books_by_title(book_category_dictionary('google_books_dataset.csv'), title))
            elif Get_Books.upper() == 'P':
                publisher = input('Enter a Publisher Name: \n')
                print(get_publisher_books(publisher,book_category_dictionary('google_books_dataset.csv')))
            elif Get_Books.upper() == 'C':
                category = input('Enter a Category: \n')
                print(get_the_books_by_category(book_category_dictionary('google_books_dataset.csv'), category))                
        if first == 'GCT':
            book_title = input('What is the title of the book?\n')
            print(get_all_categories_for_book_title(book_title,book_category_dictionary('google_books_dataset.csv')))
        if first == 'A':
            title = input("\nWhat is the title of the book would you like to add? ")
            author = input("\nWhat is the author of the book would you like to add? ")
            rating = input("\nWhat is the rating of the book would you like to add? ")
            publisher = input("\nWhat is the publisher of the book would you like to add? ")
            pages = input("\nHow many pages are there in pages of the book would you like to add? ")
            catagory = input("\nWhat is the catagory of the book would you like to add? ")
            language = input("\nWhat is the language of the book would you like to add? ")
            new_tuple = (('title',title),('author',author),('rating',rating),('publisher',publisher),('pages',pages),('catagory',catagory),('language',language))
            add_book(book_category_dictionary('google_books_dataset.csv'),new_tuple)
        if first == 'R':
            title2 = input('What is the title of the book you would like to remove? ')
            category2 = input('What is the category of the book you would like to remove? ')
            remove_book(book_category_dictionary('google_books_dataset.csv'),title2,category2)
        else:
            if first not in command_list:
                print(first," is not a command.\n")    
def main_script():
    '''Makes the entire UI function by combining all of the different functions
    '''
    global x
    global a
    global dictionary
    dictionary = 0
    x = 0
    a = 0
    while (x == 0):
        main_menu()
        string = prompt_for_command()
        commands(string)
      
main_script()
