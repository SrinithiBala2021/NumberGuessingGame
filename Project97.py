import random 
print("Number Guessing Game")
number = random.randint(1,9)
print("Guess a number (betweeb 1 and 9 :")
chances=0

while chances < 5:

    guess = int(input("Enter Your Guess -"))

    if guess == number:
        print ("Congratulations you won !!!")
        break 
    elif guess < number :
        print("Your guess was too low , Guess a number higher than",guess)
    else :
        print("your guess was too high , Guess a number lower than",guess)

    chances += 1

    if not chances <5:
        print("YOU LOOSE !!! THE NUMBER IS ", number)