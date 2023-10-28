print(' 1 : To convert Celsius to Fahrenheit\n 2 : To convert Fahrenheit to Celsius\n\n')
State = int(input('Enter your choice 1 or 2 : '))
if State == 1:
    c = float(input('Enter the temperature from Celsius: '))
    f = (c * 1.8) + 32
    print(f'The temperature is: Fahrenheit {f} ')
elif State == 2:
    f = float(input('Enter your temperature from Fahrenheit: '))
    c = (f -32)/1.8
    print(f'The temperature is: Celcius {c}')
else:
    print('Invalid option enterd')
