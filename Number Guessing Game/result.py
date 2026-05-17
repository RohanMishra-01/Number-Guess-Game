from computer_choice import computer_choice
def result(guess):
    if guess==computer_choice():
        return "Won"
    else:
        return "Lost"