from result import result
from computer_choice import computer_choice

def game():
    while True:
        print("-"*20,"MENU","-"*20)
        print("Kindly enter a number, It will be checked against computer's random chosen 4 digit number if it is same you win else, you loose!! ")
        guess=input("Enter a 4 digit number: ")
        
        if type(guess)!=int:
            print("Kindly enter a number!!")
            break

        if len(str(guess))>4:
            print("Kindly enter a 4 digit number!!")
            break

        comp=computer_choice()
        print("Computer's choice: ",comp)

        outcome=result(guess)
        
        if outcome =="Won":
            print("Congratulations you guessed the correct number!!")
            break
        else:
            print("Your guess was wrong, try again !!")

game()