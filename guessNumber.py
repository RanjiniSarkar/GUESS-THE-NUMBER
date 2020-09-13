import random
print("number guessing game")
number = random.randint(1,9)
chances = 0
print("guess number between 1 to 9")
while chances<5 :
    guess = int(input("enter your guess:- "))
    if(guess == number):
        print("CONGRATULATIONS YOU WON")
        break
    elif guess<number:
        print("YOUR GUESS WAS TOO LOW", guess)
    else:
        print("YOUR GUESS WAS TOO HIGH", guess)
    chances= chances+1
if not chances<5:
    print("YOU LOOSE THE NUMBER IS ", number)