Num01 = float(input('Enter your first number :'))
Num02 = float(input('Enter your second number :'))
Opt = input("Enter your operation : ")

try:
    if Opt == "+":
        Ans = Num01 + Num02
        print('Result : ', Ans)
    elif Opt == "-":
        Ans = Num01 - Num02
        print('Result : ', Ans)
    elif Opt == "*":
        Ans = Num01 * Num02
        print('Result : ', Ans)
    elif Opt == "/":
        Ans = Num01 / Num02
        print('Result : ', Ans)
    else:
        print("Invalid operation")
        
except ZeroDivisionError:
    print('Error!!')
