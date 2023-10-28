# Importing random function
import random

# Variables
dice_count = 0

# Rolling the dices
for i in range(101):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    if dice1 == dice2:
        dice_count += 1
print("You are out of 100 rolls", dice_count , "double")
