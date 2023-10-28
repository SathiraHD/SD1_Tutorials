n = input('Please enter an integger: ')
try:
    n = int(n)
    print(n)
except ValueError:
    print('Requires a valid integer!')
