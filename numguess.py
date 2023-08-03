print("Welcome to guess number!")

import random

pc_number = random.randint(0,20)

for i in range(10):
    user_number = int(input("enter your number (you can guess 10 times at max): "))

    if user_number == pc_number :
        print("well done! you guessed the correct number after" , i , "time(s)")
        break
    if user_number < pc_number :
        print("wrong! go higher!")
    if user_number > pc_number :
        print("wrong! go lower!")
          
