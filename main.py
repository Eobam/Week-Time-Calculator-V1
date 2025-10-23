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
    m_number = (int(random_time_choice())) 
    m_book = (random_book_choice())
    tu_number = (int(random_time_choice()))
    tu_book = random_book_choice()
    wed_number = (int(random_time_choice()))
    wed_book = random_book_choice()
    th_number = (int(random_time_choice())) 
    th_book = random_book_choice()
    fr_number = (int(random_time_choice()))
    fr_book = random_book_choice()
    sa_number = (int(random_time_choice()))
    sa_book = random_book_choice()
    su_number = (int(random_time_choice()))
    su_book = random_book_choice()
    output = m_number + tu_number + wed_number + th_number + fr_number + sa_number + su_number

    print("Total time calculated", output)

    if any(day > max_daily_minutes for day in [m_number, tu_number, wed_number, th_number, fr_number, sa_number, su_number]):
        continue

    if output == total_time:
        total_time_correct = True
        daily_time_book()
        print("monday", m_number, m_book)
        print("tuesday",tu_number, tu_book)
        print("wednesday", wed_number, wed_book)
        print("thursday", th_number, th_book)
        print("friday", fr_number, fr_book)
        print("saturday", sa_number, sa_book)
        print("sunday", su_number, su_book)
        break

