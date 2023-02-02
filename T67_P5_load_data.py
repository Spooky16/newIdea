#Written by Grant Phillips 101230563

def book_category_dictionary(filename: str) -> dict:
    ''' Function Takes in a filename, returns a dictionary with the keys as the catagories from the file, and the values as lists of dictionaries for all the individual books
    >>>len(book_category_dictionary(google_books_dataset.csv))   ** Note: Was unsure how to test file, TA in discord said to display the length
    26
    '''
    infile = open(filename,'r')
    next(infile)
    book_dictionary = {}
    title_set = {*()}
    catagory_list = ['Adventure','Biography','Business','Classics','Comics','Crime','Detective','Economics','Epic','Fantasy','Fiction','Finance','Horror','Humor','Information Technology','Investing','Legal','Management','Money Management','Mystery','Mythical Creatures','Psychology','Social Science','Superheroes','Thrillers','Traditional']
    d = {} #new_dict
    for x in range(0, 26):
        d[x] = {} 
    b = {} #empty_lst
    for y in range(0, 26):
        b[y] = []
    c = {}#lst
    for z in range(0, 26):
        c[z] = []    
        
    for line in infile:
        current_catagory = line.split(",")[5]
        #title_set.clear()
        for i in range(0,26):
            if current_catagory == catagory_list[i]:
                x = i
        temp_tup = (line.split(",")[0],line.split(",")[5])
        #print(temp_tup)
        
        #print(title_set)
        if temp_tup not in title_set:
            c[x] = []
            book_dictionary[current_catagory] = c[x]
            d[x] = {} 
            d[x] ["title"] = line.split(",")[0]
            #print(temp_tup)
            d[x] ["author"] = line.split(",")[1]
            
            rating = line.split(",")[2]
            if rating != 'N/A':
                d[x] ["rating"] = float(rating)
            else:
                d[x] ["rating"] = line.split(",")[2]
                
            d[x] ["publisher"] = line.split(",")[3]
            pages = line.split(",")[4]
            d[x] ["pages"] = int(pages)
            d[x] ["langugage"] = line.strip("\n").split(",")[6]
            book_dictionary[current_catagory] = b[x] 
            c[x]  += [d[x]] 
            book_dictionary[current_catagory] += c[x]
        title_set.add(temp_tup)
    infile.close()
    return book_dictionary
book_category_dictionary('google_books_dataset.csv')



