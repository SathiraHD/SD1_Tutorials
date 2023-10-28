Response = str(input('Do you like Python?  (Yes or No) : ')).lower()
if Response == 'yes' or Response == 'y' :
    print('You are on the right course.')
elif Response == 'no' or Response == 'n' :
    print('You might change your mind.')
else:
    print('I did not understand')
