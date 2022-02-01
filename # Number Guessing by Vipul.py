# Number Guessing by Vipul

import random
playing = input("What is your Name:" )

playing = input("Do you want to play:" )
if playing != ("yes"):
    print("please type yes next time")
    quit()
    

    
random_number = random.randrange(0,51)
print("Select a random number betweeen 0-50")
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number")
        continue

    if user_guess > random_number:
        print("You are Above the Number !")

    elif user_guess < random_number:
        print("You are Below the Number !")

    elif user_guess == random_number:
        print("You got it in", guesses,"Guesses")        
        break
        

