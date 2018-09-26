import random
print("Are you ready to play the number guessing game?")
print("Guess a number between 1 and 9. If you want to quit, type 'exit'")
random_number = random.randint(1,9)
user_guess = 0
count = 1

while (user_guess!= random_number):
    user_guess = input("What's your guess?")
    if user_guess == "exit":
        print("You decided to end the game! Thanks for your time")
        break

    user_guess = int(user_guess)
    if user_guess < random_number:
        print("Enter a bigger number") 
        count += 1
    elif user_guess > random_number:
        print("Enter a lesser number") 
        count += 1
    else:
        print("You took only %d trial(s) and guessed it right. Good job!" %count )
