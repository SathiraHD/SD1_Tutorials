import random

hidden = random.randint(1,20)
guess = int(input('Enter guess number between 1 to 20 : '))
while (guess != hidden):
    print('Your guess is not correnct, Try again!!')
    guess = int(input('Enter guess number between 1 to 20 : '))
    break
print('Congratulation!! Your guess was correct')
