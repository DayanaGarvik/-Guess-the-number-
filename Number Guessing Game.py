import random

number_of_guesses = 0

num = random.randint(1, 20)
answer = input("Do you want to play a game? Yes or No? ").lower()
while answer == "Yes".lower():
    number_of_guesses += 1
    guess = int(input("Choose a number between 1 and 20, or write '100' to quit: "))
    if guess < num and guess != 100:
        print("Too low, try again!")
    elif guess > num and guess != 100:
        print("Too high, try again!")
    elif guess == num and guess != 100:
        print("Heeey, you got it! It only took ", number_of_guesses, " guesses!")
        break
    elif guess == 100:
        print("Ok, It was fun playing with you!")
        break

if answer == "No".lower():
    print("Oh well, maybe next time!")