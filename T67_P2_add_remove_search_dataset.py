#T67 Grant Phillips
from T67_P5_load_data import book_category_dictionary

#The 8 Functions

def add_book(dictionary: dict, book: tuple) -> dict: #Grant Phillips 101230563
    '''
    Function takes in a dictionary and a tuple as arguments, the tuple contains the information of a new book which the function adds to the dictionary being passed through in the proper catagory. The function returns the new updated dictionary with the new book added in, as well as verifies that the new book has been added correctly and display the result via a print out
    >>>add_book(book_category_dictionary('google_books_dataset.csv'),(('title','example'),('author','example'),('rating','example'),('publisher','example'),('pages','example'),('catagory','Fiction'),('language','example')))
    '''
    new_dictionary = dict((key,value)for key,value in book)
    catagory = new_dictionary['catagory']
    del new_dictionary['catagory']
    dictionary[catagory] += [new_dictionary]
    a = len(dictionary[catagory])
    x = 0
    for item in dictionary[catagory]:
        if new_dictionary == item:
            print('The book has been added correctly')
        else:
            x += 1
    if a == x:
        print('There was an error adding the book')
    return dictionary

def remove_book(dictionary: dict, title: str, catagory: str) -> dict: #Grant Phillips 101230563
    '''
    Function takes in a dictionary, book title, and book catagory as the arguments. Function removes the book with the passed title under the proper catagory within the passed dictionary. Function returns the dictionary as well as a confirmation that the book has been correctly removed via a print out.
    >>>remove_book(dictionary,'example','Fiction')
    '''
    a = len(dictionary[catagory])
    x=0
    for item in dictionary[catagory]:
        if item['title'] == title:
            removed = dictionary[catagory].pop(x)
            print('book has been removed correctly')
        else:
            x += 1
        if x == a:
            print('There was an error removing the book. Book not found.')
    return dictionary

def get_books_by_title(dictionary: dict, title: str): #Aidan Karst 101239769
    '''
    Returns if a given book is in the dictionary or not. Will either return "True, the book is in the dictionary", or "False, the book could not be located in the dictionary".
    
    >>> get_books_by_title(books_by_title,'Bring Me Back')
    True, the book is in the dictionary
    
    >>> get_books_by_title(books_by_title,'The Hobbit')
    False, the book could not be located in the dictionary
    
    >>> get_books_by_title(books_by_title,'Ultimate Spider-Man Vol. 11: Carnage')
    True, the book is in the dictionary
    
    '''
    c = 0
    dictionary_book_list = dictionary.values()
    for row in dictionary_book_list:
        for column in row:
            if column.get("title") == title:
                c = 1
                "{i}, the book is in the dictionary".format(i = bool(column.get("title") == title))
                return True
    if c == 0:       
        print("{i}, the book could not be located in the dictionary".format(i = bool(column.get("title") == title)))
        return False


def get_books_by_author(dictionary: dict, author_name: str) -> int: #Aidan Karst 101239769
    '''
    Returns the book titles of a given author. Will return "The author [name] has published the following books:".
    
    >>> get_books_by_author(author_books, 'Brandon Sanderson')
    The author Brandon Sanderson has published the following books:
       Book 1 : Edgedancer: From the Stormlight Archive , Rating: 4.8
       Book 2 : Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages , Rating: 4.7
    2
       
    >>> get_books_by_author(author_books, 'Barbara Allan')
    The author Barbara Allan has published the following books:
       Book 1 : Antiques Chop , Rating: 4.5
       Book 2 : Antiques Roadkill: A Trash 'n' Treasures Mystery , Rating: 3.3
       Book 3 : Antiques Knock-Off , Rating: 4.3
       Book 4 : Antiques Con , Rating: 4.8
    4
    
    >>> get_books_by_author(author_books, 'Andrzej Sapkowski')
    The author Andrzej Sapkowski has published the following books:
       Book 1 : Sword of Destiny: Witcher 2: Tales of the Witcher , Rating: 4.8
       Book 2 : The Tower of the Swallow: Witcher 6 , Rating: 4.6
       Book 3 : The Malady and Other Stories: An Andrzej Sapkowski Sampler , Rating: 4.8
    3
    
    '''
    
    final_list = []
    for z in dictionary:
        for value in dictionary[z]:
            if author_name == value['author']:
                final_list.append((value['title'], value['rating']))
                final_list = list(set(final_list))
    print("The author", author_name, "has published the following books:")
    for i in range(len(final_list)):
        print("   Book", str(i + 1), ":", final_list[i][0], ", Rating:", final_list[i][1])
    return len(final_list)



def get_publisher_books(publisher_name:str, dictionary: dict): #Mikhali Shahid 101232932
   
    '''
    Returns books published by a publisher. 
    >>> get_publisher_books('Kensington Publishing Corp', books_of_publisher)
   The publisher Kensington Publishing Corp. has published the following books:
   Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery
   Book 2: Antiques Knock-Off
   Book 3: Antiques Knock-Off
   Book 4: Antiques Roadkill: A Trash 'n' Treasures Mystery
   Book 5: Antiques Knock-Off
   Book 6: Antiques Roadkill: A Trash 'n' Treasures Mystery
    '''
    list_final=[]    
    temp_lst=[]
    num = 0
    for value in dictionary.values():
        for dictionary in value:
            if dictionary.get('publisher') == str(publisher_name):
                if dictionary.get('title') not in temp_lst:
                    list_final.append(dictionary.get('title'))
                    temp_lst += [dictionary.get('title')]
    print('The publisher ' + str(publisher_name) + ' has published the following books:')
    for title in list_final:
        num += 1
        print( 'Book ' +str(num) +': ' + title)
    return len(list_final)


def get_all_categories_for_book_title(book_title:str, dictionary: dict): #Mikhali Shahid 101232932
    '''
    Returns categories of a title.
    >>> get_all_categories_for_book_title('After Anna', titles_under_category)
   The book title After Anna belongs to the following categories:
   Category 1: "fiction"
   Category 2: "adventure"
   Category 3: "thriller"
   Category 4: "mystery"
    '''    
    list_final=[]
    temp_lst=[]
    num = 0
    for value in dictionary:
        for item in dictionary[value]:
            if item['title'] == str(book_title):
                if value not in temp_lst:
                    list_final.append(value)
                    temp_lst +=[value]
    print('The book title ' + str(book_title) + ' belongs to the following categories:')
    for category in list_final:
        num += 1
        print( 'Category ' +str(num) +': ' + category)
    return len(list_final)


def get_the_books_by_category(kk,search_cate): #Pongwit Phutragulpant 101224008
    #kk is a dict, search_cate is a string
    cate_book_list = []
    for book in kk[search_cate]:
        cate_book_list.append(book)      #put every book that has the same category in the same Array List
    print('The category "{}" has {} books. This is the list of books:\n' .format(search_cate,len(cate_book_list)))
    for index in range(len(cate_book_list)):
        cate_book = cate_book_list[index]
        print('Book {} : "{}" by "{}" '.format(index+1,cate_book["title"],cate_book["author"]))
    print('\n')
    return len(cate_book_list)
   



def get_books_by_rate (kk,rate_range): #Pongwit Phutragulpant 101224008

    lower_rate = rate_range
    upper_rate = rate_range + 1
    wanted_books_list = []

    for i in range(len(list(kk.values()))):  
            for j in range(len(list(kk.values())[i])):
                    if list(kk.values())[i][j]["rating"] != "N/A":
                        if list(kk.values())[i][j]["rating"] >= lower_rate and list(kk.values())[i][j]["rating"] < upper_rate:
                                wanted_books_list.append(list(kk.values())[i][j])

    baked_book = []
    for v in range(len(wanted_books_list)):
            if wanted_books_list[v] not in baked_book:
                    baked_book.append(wanted_books_list[v])

    print("There are {} books whose rate is between {} and {} . This is the list of books:".format(len(baked_book),lower_rate,upper_rate))
       
    for index in range(len(baked_book)):
            print('Book {} : "{}" by "{}" '.format(index+1,baked_book[index]["title"],baked_book[index]["author"]))
    print('\n')
    return len(baked_book)

'''

#Tests
def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, "
              "but outcome ({3}) has type {4}\n".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return 0
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}\n".
              format(description, expected, outcome))
        return 0
    else:
        print("{0} PASSED\n".format(description))
        return 1
    print("------")

def test_get_books_by_publisher() -> None: #Grant Phillips 101230563
    Test case for the get_books_by_publisher function
    
    #Test1 get_books_by_publisher(dictionary,publisher) because the publisher has the same book across different catagories and it is important to make sure the function isn't returning duplicates.
    #Test2 get_books_by_publisher(dictionary,greatPublisher) because the publisher has multiple different books across different catagories and a large amount of books, important it collects all the individual books without duplicates
    #Test3 get_books_by_publisher(dictionary,badPublishing) this publisher only has one book, this test ensures the function can handle not only large values like the test above it, but also returning only small values
    #Test4 get_books_by_publisher(dictionary,thePublisher) because this publisher has nothing special about it, a test to make sure the function can handle a basic call and reensure it works as its supposed to 
    
    total_test = 0
    test_pass = 0    
    
    test_pass += check_equal('get_publisher_books(book_category_dictionary,HarperCollins UK)',get_publisher_books('HarperCollins UK',book_category_dictionary('google_books_dataset.csv')),12)
    total_test += 1
    test_pass += check_equal('get_publisher_books(book_category_dictionary,Hachette UK)',get_publisher_books('Hachette UK',book_category_dictionary('google_books_dataset.csv')),12)
    total_test += 1
    test_pass += check_equal('get_publisher_books(book_category_dictionary,Red Wheel/Weiser)',get_publisher_books('Red Wheel/Weiser',book_category_dictionary('google_books_dataset.csv')),1)
    total_test += 1
    test_pass += check_equal('get_publisher_books(book_category_dictionary,Penguin)',get_publisher_books('Penguin',book_category_dictionary('google_books_dataset.csv')),5)
    total_test += 1
    
    return (total_test,test_pass)

def test_get_all_categories_for_book_title() -> None: #Grant Phillips 101230563
    Test case for the get_all_categories_for_book_title function
    
    #Test1 get_books_by_publisher(dictionary,publisher) because the book exsists across multiple categories, and it is important to make sure the function properly accounts for them all
    #Test2 get_books_by_publisher(dictionary,greatPublisher) because the book only has one specific category, it is important for the function to be able to handle small values and still return the same output
    #Test3 get_books_by_publisher(dictionary,badPublishing) because this test is a final test to make sure the function works as intended too, nothing special about the book title
    #Test4 get_books_by_publisher(dictionary,badPublishing) because there isnt a book by the name of this title, checking to see if the function can handle having nothing to return
    
    total_test = 0
    test_pass = 0    
 
    test_pass += check_equal('get_all_categories_for_book_title(book_category_dictionary,The Memoirs of Sherlock Holmes)',get_all_categories_for_book_title('The Memoirs of Sherlock Holmes',book_category_dictionary('google_books_dataset.csv')),5)
    total_test += 1
    test_pass += check_equal('get_all_categories_for_book_title(book_category_dictionary,Venomized)',get_all_categories_for_book_title('Venomized',book_category_dictionary('google_books_dataset.csv')),1)
    total_test += 1
    test_pass += check_equal('get_all_categories_for_book_title(book_category_dictionary,The Black Box)',get_all_categories_for_book_title('The Black Box',book_category_dictionary('google_books_dataset.csv')),4)
    total_test += 1
    test_pass += check_equal('get_all_categories_for_book_title(book_category_dictionary,The Grant Book)',get_all_categories_for_book_title('The Grant Book',book_category_dictionary('google_books_dataset.csv')),0)
    total_test += 1

    return (total_test,test_pass)
#(total,passed) = test_get_books_by_publisher() #Grant Phillips 101230563
#(total1,passed1) = test_get_all_categories_for_book_title() #Grant Phillips 101230563



passed2 = check_equal('Book exists test', get_books_by_title(book_category_dictionary('Google_Books_Dataset.csv'),'The Black Box'), True) #Mikhali Shahid 101232932
passed3 = check_equal('Number of books by author', get_books_by_author(book_category_dictionary('Google_Books_Dataset.csv'),'Andrzej Sapkowski'),3) #Mikhali Shahid 101232932


(passed4) = check_equal('Category Function Test', get_the_books_by_category(book_category_dictionary('google_books_dataset.csv'),'Adventure'),7) #Aidan Karst 101239769
(passed5) = check_equal('Rate Function Test', get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),5),5) #Aidan Karst 101239769
 
def test_add_book(): #Pongwit Phutragulpant 101224008
    passed = 0
    test = 0
    add_book = (('title','example'),('author','example'),('rating','example'),('publisher','example'),('pages','example'),('catagory','Fiction'),('language','example'))
    #test PASSED
    passed +=check_equal('title','example','example')
    test += 1
    passed +=check_equal('author','example','example')
    test += 1
    passed +=check_equal('rating',5.20,5.20)
    test += 1
    passed +=check_equal('publisher','example','example')
    test += 1
    passed +=check_equal('pages',2,5)
    test += 1
    passed +=check_equal('catagory','example','example')
    test += 1
    passed +=check_equal('language','example','example')
    test += 1
    #test FAILED
    passed +=check_equal('title',50,'example')
    test += 1
    passed +=check_equal('author',5.3,'example')
    test += 1
    passed +=check_equal('rating','example',5.20)
    test += 1
    passed +=check_equal('publisher',8.0,'example')
    test += 1
    passed +=check_equal('pages','example',5)
    test += 1
    passed +=check_equal('catagory',5,'example')
    test += 1
    passed +=check_equal('language',5,'example')
    test += 1
    return (passed,test)
(passed6,test) = test_add_book()

def test_remove_book(): #Pongwit Phutragulpant 101224008
    passed = 0
    test = 0
    remove_book = (('title','str'),('author','example'),('rating','example'),('publisher','example'),('pages','example'),('catagory','str'),('language','example'))
    #test PASSED
    passed +=check_equal('title','example','example')
    test += 1
    passed +=check_equal('author','example','example')
    test += 1
    passed +=check_equal('rating',5.20,5.20)
    test += 1
    passed +=check_equal('publisher','example','example')
    test += 1
    passed +=check_equal('pages',2,5)
    test += 1
    passed +=check_equal('catagory','example','example')
    test += 1
    passed +=check_equal('language','example','example')
    test += 1
    
    #test FAILED
    passed +=check_equal('title',50,'example')
    test += 1
    passed +=check_equal('author',5.3,'example')
    test += 1
    passed +=check_equal('rating','example',5.20)
    test += 1
    passed +=check_equal('publisher',8.0,'example')
    test += 1
    passed +=check_equal('pages','example',5)
    test += 1
    passed +=check_equal('catagory',5,'example')
    test += 1
    passed +=check_equal('language',5,'example')
    test += 1
    return (passed,test)
(passed7,test1) = test_remove_book()


print(passed+passed1+passed2+passed3+passed4+passed5+passed6+passed7,'tests have passed out of the',total+total1+passed2+passed3+passed4+passed5+test+test1,'that have occurred\n')
'''
