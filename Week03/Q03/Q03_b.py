Num01 = int(input('Enter the first number : '))
Num02 = int(input('Enter the second number : '))
Opt = str(input('Enter the operation what you need : '))
if Opt == "+":
    Ans = Num01 + Num02
    print(Ans)
elif Opt == "-":
    Ans = Num01 - Num02
    print(Ans)
elif Opt == "*":
    Ans = Num01 * Num02
    print(Ans)
else:
    Ans = Num01 / Num02
    print(Ans)
