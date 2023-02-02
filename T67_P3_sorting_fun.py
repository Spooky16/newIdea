#T67 Grant Phillips 101230563 , Aidan Karst 101239769 , Mikhali Shahid 101232932 , Pongwit Phutragulpant 101224008 2022/04/10 Version 1.0
from T67_P5_load_data import book_category_dictionary
#from T76_check_equal import check_equal
#The 8 Functions
def dictionary_to_list(dictionary: dict) -> list:
    '''Function takes a dictionary and retruns the values as a lsit
    '''
    new_list = []
    new_set = {*()}
    for item in dictionary:
        for book in dictionary[item]:
            if book['title'] not in new_set:
                new_list += [book]
            new_set.add(book['title'])
    return new_list



def sort_books_title(dictionary:dict)-> list: #Grant Phillips 101230563
    '''Function takes in a dictionary containing list of books based off category, returns a list sorted alphabetically (with special characters at the front) by the book title containing all the books with no duplicate entires and the category part of the dictionary as a list of all the categories the book is in,
    >>>sort_books_title(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'langugage': 'English', 'category': ['Fiction', 'Thrillers']},....{'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'langugage': 'English', 'category': ['Comics', 'Superheroes']}]
    '''
    new_dict = {}
    title_set = {*()}
    for item in dictionary:
        for val in dictionary[item]:
            lst1 = []
            a = val['title']
            if val['title'] not in title_set:
                new_dict[a] = lst1
            lst1 = item
            new_dict[a] += [lst1]
            title_set.add(val['title'])
    big_lst = dictionary_to_list(dictionary)        
    #big_lst = [] Wasn't nessiscary with new dictionary to list function
    #title_set2 = {*()} Wasn't nessiscary with new dictionary to list function
    for item in dictionary:
        for val in dictionary[item]:
            val['category'] = []
            val['category'] = new_dict[val['title']]
            #if val['title'] not in title_set2: Wasn't nessiscary with new dictionary to list function
                #big_lst += [val] Wasn't nessiscary with new dictionary to list function
            #title_set2.add(val['title']) Wasn't nessiscary with new dictionary to list function
            
    a = len(big_lst)
    for i in range(a):
        for j in range(0,a-i-1):
            if big_lst[j]['title'] > big_lst[j+1]['title']:
                big_lst[j], big_lst[j+1] = big_lst[j+1], big_lst[j]
    return big_lst

def sort_books_author(dictionary:dict)->list: #Mikhali Shahid 101232932

    lst = dictionary_to_list(dictionary)

    a = len(lst)
    for i in range(a):
        for j in range(0, a-i-1):
            if lst[j+1]['author'] < lst[j]['author']:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        

    return lst

def sort_books_ascending_rate(book_dictionary: dict) -> list: #Aidan Karst 101239769
    """
    Returns a list with the book data stored as a dictionary where the books are sorted by the rate in ascending order. The rating 0 equates to the N/A rating.
    
    >>> sort_books_ascending_rate(book_dictionary)
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'langugage': 'English', 'category': ['Fiction', 'Detective', 'Mystery']}, ... (and so on)

    """
    listofbooks = []
    n = len(listofbooks)
    i = 0
    
    for z in book_dictionary:
            for b in book_dictionary[z]:
                previous_added = False
                for book_added in listofbooks:
                    if book_added['title'] == b['title']:
                        previous_added = True
                        book_added['category'].append(z)
                if not previous_added:
                    cate = b
                    cate['category'] = [z]
                    listofbooks.append(cate)
    a = len(listofbooks)
    for i in range(a):
        for j in range(0,a-i-1):
            if listofbooks[j]["rating"] == "N/A":
                listofbooks[j]["rating"] = 0   
            if listofbooks[j+1]["rating"] == "N/A":
                listofbooks[j+1]["rating"] = 0            
            if listofbooks[j]['rating'] > listofbooks[j+1]['rating']:
                listofbooks[j], listofbooks[j+1] = listofbooks[j+1], listofbooks[j]                  
    return listofbooks
    

def sort_books_publisher(dictionary): #Pongwit Phutragulpant 101224008
    '''
    Function takes in a dictionary and , return list by sorting books alphabetically by publisher in the bubble sorting format. 
    
    '''    
    new_list = dictionary_to_list(dictionary)  
    a = len(new_list)
    
    for i in range(a):
        for j in range(0,a-i-1):
            if new_list[j]['publisher'] > new_list[j+1]['publisher']:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list

#Testing Functions

def testing_sort_books_ascending_rate(): #Grant Phillips 101230563
    '''Test case for sort_books_ascending_rate
    '''
    '''
    #Test1 sort_books_ascending_rate1(book_category_dictionary('example1.csv')) This test contains a new set of data to ensure that the function is working properly and sorting in an ascending fashon.
    #Test2 sort_books_ascending_rate2(book_category_dictionary('example2.csv')) This test also contains a whole new set of data but contains some books with the rating of 0 and n/a to make sure it can handle the float vs string comparison issue
    #Test3 sort_books_ascending_rate2(book_category_dictionary('example2.csv')) This test makes sure the function returns the proper object type
    
    total_test = 0
    test_pass = 0   
    test_pass += check_equal('check type(sort_books_author)', type(sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv'))), list)
    total_test += 1
    test_pass += check_equal('sort_books_ascending_rate(book_category_dictionary("example1.csv")',sort_books_ascending_rate(book_category_dictionary('example1.csv')),[{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'langugage': 'English', 'category': ['Comics']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'langugage': 'English', 'category': ['Fiction']}])
    total_test += 1
    test_pass += check_equal('sort_books_ascending_rate(book_category_dictionary)',sort_books_ascending_rate(book_category_dictionary('example2.csv')),[{'title': 'Summary', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'langugage': 'English', 'category': ['Business','English']},{'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown', 'rating': 0.0, 'publisher': 'Random House', 'pages': 576, 'langugage': 'English', 'category': ['Social Science']}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 0.0, 'publisher': 'HarperCollins UK', 'pages': 208, 'langugage': 'English', 'category': ['Detective']}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'langugage': 'English', 'category': ['Mystery']}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'langugage': 'English', 'category': ['Thrillers']}])
    total_test += 1
    
    return (total_test,test_pass)
(total,passed) = testing_sort_books_ascending_rate()

def testing_sort_books_publisher(): #Mikhali Shahid 101232932
    total_test = 0
    test_pass = 0     
    test_pass += check_equal('sort_books_publisher(book_category_dictionary("example1.csv"))',sort_books_publisher(book_category_dictionary("example1.csv")),[{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'langugage': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'langugage': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'langugage': 'English'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'langugage': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'langugage': 'English'}])
    total_test += 1
    return (total_test,test_pass)
(total1,passed1) = testing_sort_books_publisher()


def test_get_books_by_author()-> None: #Pongwit Phutragulpant 101224008
    """
    Test case for the get_books_by_author
    """
    #First test is to check type of the function suppose to be dictionary
    #Second test the lens of the or number of author
    #Third.Forth,Fifth test is to check sort order of the author
    total_test = 0
    test_pass = 0
    test_pass += check_equal('check type(sort_books_author)', type(sort_books_author(book_category_dictionary('google_books_dataset.csv'))), list)
    total_test += 1
    test_pass += check_equal('check number of author(sort_books_author)',(len(sort_books_author(book_category_dictionary('google_books_dataset.csv')))),5)
    total_test += 1
    test_pass += check_equal('sort_books_author(book_category_dictionary("example1.csv"))', sort_books_author(book_category_dictionary('example1.csv')),[{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'langugage': 'English', 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'langugage': 'English', 'category': ['Comics']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'langugage': 'English', 'category': ['Fiction']}])
    total_test +=1
    return(total_test,test_pass)

(total2,passed2) = test_get_books_by_author()


def testing_sort_books_title(): #Aidan Karst 101239769
    total_test = 0
    test_pass = 0    
    test_pass =  check_equal('Function First Test',sort_books_title(book_category_dictionary('example1.csv')),[{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'langugage': 'English', 'category': ['Comics']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'langugage': 'English', 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'langugage': 'English', 'category': ['Fiction']}])
    total_test += 1
    return (total_test,test_pass)
(total3,passed3) = testing_sort_books_title()

print('The functions passed',passed+passed1+passed2+passed3,'of the tests, the functions failed',total+total1+total2+total3-(passed+passed1+passed2+passed3),'of the tests, a total of',total+total1+total2+total3,'Tests have happened')
'''