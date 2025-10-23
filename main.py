#Imports
import random

#global inputs
total_time = int(input("How many minutes do you want?"))
max_daily_minutes = int(input("What is the maximum amount of minutes you would like in a day?"))

#Books
books = ["Example", "Example2", "Example3" ]

#Possible times for each day
times = [ 0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

#Choosing one of the times
def random_time_choice():
    new_time = random.choice(times)
    return new_time

#Choose a random book for each day
def random_book_choice():
    book = random.choice(books)
    return book

#Like the stuff that is important that combines things.
def daily_time_book():
   pass
    



total_time_correct = False
#Main
while total_time_correct == False:
    book = random_book_choice()
    new_time = random_time_choice()
    m = (new_time, book)
    book = random_book_choice()
    new_time = random_time_choice()
    tu = (new_time, book)
    book = random_book_choice()
    new_time = random_time_choice()
    wed = (new_time, book)
    book = random_book_choice()
    new_time = random_time_choice()
    th = (new_time, book)
    book = random_book_choice()
    new_time = random_time_choice()
    fr = (new_time, book)
    book = random_book_choice()
    new_time = random_time_choice()
    sa = (new_time, book)
    book = random_book_choice()
    new_time = random_time_choice()
    su = (new_time, book)
    print("test")
    break

if m + tu + wed + th + fr + sa +su == total_time:
    total_time_correct = True

if total_time_correct == True:
    daily_time_book()
    print(m)
    print(tu)
    print(wed)
    print(th)
    print(fr)
    print(sa)
    print(su)

