num1 = input('Enter an integer: ')
num2 = input('Enter an another integer which you want to divide: ')
try:
    num1 = int(num1)
    num2 = int(num2)
except ZeroDivisionError:
    print('Invalid,Cannot divide by zero!')
