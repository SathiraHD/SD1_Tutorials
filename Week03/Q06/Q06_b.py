try:
    age = input('Enter your age.')
    age = int(age)
    if age >= 18:
        print('You can vote')
    else:
        print('You can not vote yet')
except ValueError:
    print('Invalid input, Please enter a valid  input')
