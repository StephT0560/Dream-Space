import requests
import json
import random

#API Key
api_key = 'AIzaSyD3e2PdtIRdu1Ephmo2CYmZz1Yde77HhNY'

# URL to be used for searches
base_url = 'https://www.googleapis.com/books/v1/volumes?q='

# User Inputs

def user_inputs():
    in_genre = input("Write a genre you want a recommendation based on: ")
    in_author = input("Write the first and last name of an author you want a recommendation based on: ")
    in_book = input("Write the name of the book (followed by a semicolon and space) then the author you want a recommendation based on: ")
    return (in_genre, in_author, in_book)


def genre_recs(genre):
    # if the user doesn't put in a genre
    if genre == "":
        return None

    # dictionary conatining key info about books to give to users
    final_recs = {
        'Title': [],
        'Author': [],
        'Genre': [],
        'Page_Count': [],
        'Average_Rating': [],
        'Ratings_Count': [],
        'Language': [],
        'Description': [],
        'Image_Link': []
    }

    # clean up user genre input; *need a try-catch here for genres that can't be found/don't exist*
    genre = genre.lower()
    genre = genre.replace(" ", "+")

    # use api for list of book_recs
    search_recs = requests.get(base_url + 'subject:' + genre + '&maxResults=40&key=' + api_key)
    recs = search_recs.json()
    num_books = len(recs['items']) - 1
    # parse necesarry info from book recs if there are less than five recs based on criteria

    # if there are less than 5 ore equal to 5 items in the list
    if num_books <= 5:
        for i in range(num_books):
            try:
                final_recs['Title'].append(recs['items'][i]['volumeInfo']['title'])
            except:
                final_recs['Title'].append("Title N/A")

            try:
                final_recs['Author'].append(recs['items'][i]['volumeInfo']['authors'])
            except: 
                final_recs['Author'].append("Author N/A")

            try:
                final_recs['Genre'].append(", ".join(recs['items'][i]['volumeInfo']['categories']))
            except:
                final_recs['Genre'].append("Genre N/A")

            try:   
                final_recs['Page_Count'].append(recs['items'][i]['volumeInfo']['pageCount'])
            except:
                final_recs['Page_Count'].append("Page Count N/A")
            
            try:
                final_recs['Average_Rating'].append(recs['items'][i]['volumeInfo']['averageRating'])
            except:
                final_recs['Average_Rating'].append("Rating N/A")

            try:
                final_recs['Ratings_Count'].append(recs['items'][i]['volumeInfo']['ratingsCount'])
            except:
                final_recs['Ratings_Count'].append("Ratings Count N/A")

            try:
                final_recs['Language'].append(recs['items'][i]['volumeInfo']['language'])
            except:
                final_recs['Language'].append("Language N/A")
            
            try:
                final_recs['Description'].append(recs['items'][i]['volumeInfo']['description'])
            except:
                final_recs['Description'].append("Summary N/A")

            try:
                final_recs['Image_Link'].append(recs['items'][i]['volumeInfo']['imageLinks']['smallThumbnail'])
            except:
                final_recs['Image_Link'].append("Image N/A")
    
    # if there are more than 5 items in the list
    else:
        indices = []
        h = 0
        while h < 5:
            cur = random.randint(0, num_books)
            if cur not in indices:
                indices.append(cur)
                h += 1      
        for i in indices:
            try:
                final_recs['Title'].append(recs['items'][i]['volumeInfo']['title'])
            except:
                final_recs['Title'].append("Title N/A")

            try:
                final_recs['Author'].append(recs['items'][i]['volumeInfo']['authors'])
            except: 
                final_recs['Author'].append("Author N/A")

            try:
                final_recs['Genre'].append(", ".join(recs['items'][i]['volumeInfo']['categories']))
            except:
                final_recs['Genre'].append("Genre N/A")

            try:   
                final_recs['Page_Count'].append(recs['items'][i]['volumeInfo']['pageCount'])
            except:
                final_recs['Page_Count'].append("Page Count N/A")
            
            try:
                final_recs['Average_Rating'].append(recs['items'][i]['volumeInfo']['averageRating'])
            except:
                final_recs['Average_Rating'].append("Rating N/A")

            try:
                final_recs['Ratings_Count'].append(recs['items'][i]['volumeInfo']['ratingsCount'])
            except:
                final_recs['Ratings_Count'].append("Ratings Count N/A")

            try:
                final_recs['Language'].append(recs['items'][i]['volumeInfo']['language'])
            except:
                final_recs['Language'].append("Language N/A")
            
            try:
                final_recs['Description'].append(recs['items'][i]['volumeInfo']['description'])
            except:
                final_recs['Description'].append("Summary N/A")

            try:
                final_recs['Image_Link'].append(recs['items'][i]['volumeInfo']['imageLinks']['smallThumbnail'])
            except:
                final_recs['Image_Link'].append("Image N/A")

    # return dictionary with important info
    return final_recs




def author_recs(author):
        # if the user doesn't put in a genre
    if author == "":
        return None

    # dictionary conatining key info about books to give to users
    final_recs = {
        'Title': [],
        'Author': [],
        'Genre': [],
        'Page_Count': [],
        'Average_Rating': [],
        'Ratings_Count': [],
        'Language': [],
        'Description': [],
        'Image_Link': []
    }

    # clean up user genre input; *need a try-catch here for genres that can't be found/don't exist*
    author = author.lower()
    author = author.replace(" ", "+")

    # use api for list of book_recs
    search_recs = requests.get(base_url + 'inauthor:' + author + '&maxResults=40&key=' + api_key)
    recs = search_recs.json()
    num_books = len(recs['items']) - 1
    # parse necesarry info from book recs if there are less than five recs based on criteria

    # if there are less than 5 ore equal to 5 items in the list
    if num_books <= 5:
        for i in range(num_books):
            try:
                final_recs['Title'].append(recs['items'][i]['volumeInfo']['title'])
            except:
                final_recs['Title'].append("Title N/A")

            try:
                final_recs['Author'].append(recs['items'][i]['volumeInfo']['authors'])
            except: 
                final_recs['Author'].append("Author N/A")

            try:
                final_recs['Genre'].append(", ".join(recs['items'][i]['volumeInfo']['categories']))
            except:
                final_recs['Genre'].append("Genre N/A")

            try:   
                final_recs['Page_Count'].append(recs['items'][i]['volumeInfo']['pageCount'])
            except:
                final_recs['Page_Count'].append("Page Count N/A")
            
            try:
                final_recs['Average_Rating'].append(recs['items'][i]['volumeInfo']['averageRating'])
            except:
                final_recs['Average_Rating'].append("Rating N/A")

            try:
                final_recs['Ratings_Count'].append(recs['items'][i]['volumeInfo']['ratingsCount'])
            except:
                final_recs['Ratings_Count'].append("Ratings Count N/A")

            try:
                final_recs['Language'].append(recs['items'][i]['volumeInfo']['language'])
            except:
                final_recs['Language'].append("Language N/A")
            
            try:
                final_recs['Description'].append(recs['items'][i]['volumeInfo']['description'])
            except:
                final_recs['Description'].append("Summary N/A")

            try:
                final_recs['Image_Link'].append(recs['items'][i]['volumeInfo']['imageLinks']['smallThumbnail'])
            except:
                final_recs['Image_Link'].append("Image N/A")
    
    # if there are more than 5 items in the list
    else:
        indices = []
        h = 0
        while h < 5:
            cur = random.randint(0, num_books)
            if cur not in indices:
                indices.append(cur)
                h += 1      
        for i in indices:
            try:
                final_recs['Title'].append(recs['items'][i]['volumeInfo']['title'])
            except:
                final_recs['Title'].append("Title N/A")

            try:
                final_recs['Author'].append(recs['items'][i]['volumeInfo']['authors'])
            except: 
                final_recs['Author'].append("Author N/A")

            try:
                final_recs['Genre'].append(", ".join(recs['items'][i]['volumeInfo']['categories']))
            except:
                final_recs['Genre'].append("Genre N/A")

            try:   
                final_recs['Page_Count'].append(recs['items'][i]['volumeInfo']['pageCount'])
            except:
                final_recs['Page_Count'].append("Page Count N/A")
            
            try:
                final_recs['Average_Rating'].append(recs['items'][i]['volumeInfo']['averageRating'])
            except:
                final_recs['Average_Rating'].append("Rating N/A")

            try:
                final_recs['Ratings_Count'].append(recs['items'][i]['volumeInfo']['ratingsCount'])
            except:
                final_recs['Ratings_Count'].append("Ratings Count N/A")

            try:
                final_recs['Language'].append(recs['items'][i]['volumeInfo']['language'])
            except:
                final_recs['Language'].append("Language N/A")
            
            try:
                final_recs['Description'].append(recs['items'][i]['volumeInfo']['description'])
            except:
                final_recs['Description'].append("Summary N/A")

            try:
                final_recs['Image_Link'].append(recs['items'][i]['volumeInfo']['imageLinks']['smallThumbnail'])
            except:
                final_recs['Image_Link'].append("Image N/A")

    # return dictionary with important info
    return final_recs



def book_recs(orig_book):
    if orig_book == "":
        return None

    # clean up user book input; *need a try-catch here for books that can't be found/don't exist*
    book = orig_book.lower()
    book = book.replace(" ", "+")
    separation = int(book.find(';'))
    book_title = book[0:separation]
    book_author = book[(separation+1):]


    # search for the book
    search_books = requests.get(base_url + 'intitle:' + book_title + '&inauthor:' + book_author + '&maxResults=40&key=' + api_key)
    list_books = search_books.json()
    our_book = list_books['items'][0]

    
    our_book_genre = our_book['volumeInfo']['categories'][0]

    try:
        our_book_author = our_book['volumeInfo']['authors'][0]
    except:
        our_book = list_books['items'][1]
        print("Book we found: ", our_book['volumeInfo']['title'], ", ", our_book['volumeInfo']['authors'])
        our_book_genre = our_book['volumeInfo']['categories'][0]
        our_book_author = our_book['volumeInfo']['authors'][0]

    genre_results = genre_recs(our_book_genre)
    
    author_results = author_recs(our_book_author)

    return genre_results, author_results



# Give user suggestions
def output_recs():
    out_genre, out_author, out_book  = user_inputs()
    trial = genre_recs(out_genre)
    print("Recommendations based on genre: ")
    for i in range(len(trial['Title'])):
        print(trial['Title'][i])
        print(trial['Author'][i])
        print(trial['Genre'][i])
        print(trial['Page_Count'][i])
        print(trial['Average_Rating'][i])
        print(trial['Ratings_Count'][i])
        print(trial['Language'][i])
        print(trial['Description'][i])
        print(trial['Image_Link'][i])

    trial2 = author_recs(out_author)
    print("Recommendations based on author: ")
    for i in range(len(trial2['Title'])):
        print(trial2['Title'][i])
        print(trial2['Author'][i])
        print(trial2['Genre'][i])
        print(trial2['Page_Count'][i])
        print(trial2['Average_Rating'][i])
        print(trial2['Ratings_Count'][i])
        print(trial2['Language'][i])
        print(trial2['Description'][i])
        print(trial2['Image_Link'][i])

    book_rec_genre, book_rec_author = book_recs(out_book)

    print("Recommendations based on book & genre: ", book_rec_genre['Title'])
    for i in range(len(book_rec_genre['Title'])):
        print(book_rec_genre['Title'][i])
        print(book_rec_genre['Author'][i])
        print(book_rec_genre['Genre'][i])
        print(book_rec_genre['Page_Count'][i])
        print(book_rec_genre['Average_Rating'][i])
        print(book_rec_genre['Ratings_Count'][i])
        print(book_rec_genre['Language'][i])
        print(book_rec_genre['Description'][i])
        print(book_rec_genre['Image_Link'][i])

    print("Recommendations based on book & author: ", book_rec_author['Title'])
    for i in range(len(trial['Title'])):
        print(book_rec_author['Title'][i])
        print(book_rec_author['Author'][i])
        print(book_rec_author['Genre'][i])
        print(book_rec_author['Page_Count'][i])
        print(book_rec_author['Average_Rating'][i])
        print(book_rec_author['Ratings_Count'][i])
        print(book_rec_author['Language'][i])
        print(book_rec_author['Description'][i])
        print(book_rec_author['Image_Link'][i])

    
output_recs()


"""
search = requests.get("https://www.googleapis.com/books/v1/volumes?q=inauthor:daniel+keyes&key=" + api_key)
search_results = search.json()
print(search_results['items'][0]['volumeInfo']['averageRating'])
"""
