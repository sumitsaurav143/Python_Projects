#Guessing a number between (1-10)
#SUMIT SAURAV - Python Code

import random
def main():
    print("GUESS A NUMBER B/W 1-10")
    while True:
        a = random.randint(1, 10)
        User_choice = int(input("ENTER YOUR GUESS HERE : "))
        print("RANDOM NUMBER IS : ",a)
        if User_choice == a :
            print("CORRECT GUESS !!")
            break
        elif User_choice > a :
            print("WRONG GUESS, YOU GUESSED HIGHER NUMBER !!")
        else :
            print("WRONG GUESS, YOU GUESSED LESSER NUMBER !!")


if __name__ == "__main__":
    main()