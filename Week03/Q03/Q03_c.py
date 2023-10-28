Cost = float(input('Enter the cost of the meal : '))
print(' Satisfaction level\n 1 : Totally satisfied\n 2 : Satisfied\n 3 : Dissatisfied\n\n')
State = int(input('Enter your satisfaction level from 1 to 3 : '))
if State == 1:
    Tip = Cost * 0.2
    print('Tip is ',Tip)
elif State == 2:
    Tip = Cost * 0.15
    print('Tip is ',Tip)
elif State == 3:
    Tip = Cost * 0.1
    print('Tip is ',Tip)
else:
    print(' Invalid rating level')
