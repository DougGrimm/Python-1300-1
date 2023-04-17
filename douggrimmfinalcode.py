'''Create a code that picks a number between 1-100 and make the user guess the number.
Guide the user if too high or low and count the number of tries it takes the user to guess
the correct number.'''

# Douglas Grimm
# CSIS 1300
# 4/10/2023

# generates random number
import random

# randint chooses number between 1-100
number = random.randint(1, 100)
guesses = 0

while True:
    userguess = int(input("Guess a number from 1 to 100: "))
    
    # increments everytime it loops
    guesses += 1
    
    if userguess == number:
        print(f"Correct! It took {guesses} tries to guess the number.")
        break
    elif userguess < number:
        print("Too low.")
    else:
        print("Too high.")

# Thoughts
# Definitely one of the easier codes i've had to create. Utilized the randint function to generate 
# the number and just used basic if-else statements to complete the rest of the code.