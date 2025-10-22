#Imports
import random

total_time = input("How many minutes do you want?")


#Books
books = ["Example", "Example2", "Example3" ]


#Choose a random book for each day
def random_book_choice():
    book = random.choice(books)
    return book


#Main
book = random_book_choice()
print(book)
