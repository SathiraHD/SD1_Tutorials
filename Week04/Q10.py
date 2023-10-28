import random

# Variables
Hidden = random.randint(1,20)
Guess = 0
Guess_Num = 0

# Getting input from the user
Guess = int(input("Guess the number : "))

# Process
while Guess != Hidden:
    
    if Guess < Hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    Guess_Num += 1
    if Guess_Num == 5:
        print("No more guesses left")
        print("Not guessed. The correct answer was:", Hidden)
        break
    else:
        Guess = int(input("Please try again:"))

# Output
print("You got it in", Guess_Num , "Guesses")
