#Question 4 v) 
print('(Covert str into int)')
num_1 = input('Enter number one: ')
num_2 = input('Enter number two: ')
total = (int(num_1) + int(num_2))
print(total)


print('Convert str to float')
cost = input('Enter cost of items: ')
paid = input('Enter cash paid: ')
change = (float(paid) - float(cost))
print('Change is: ', change)


print('calculate the average')
num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
num_3 = int(input('Enter the third number: '))
average = (num_1 + num_2 + num_3)/3
print('Averge is: ', round(average,3))
