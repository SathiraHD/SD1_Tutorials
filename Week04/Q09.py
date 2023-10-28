option = 0
for option in range(1,5):
    option = int(input("Enter 1, 2, or 3 to loop. 4 to Quit the program : "))
    if option == 4:
        print("Quit selected")
        break
    else:
        print(option , "selected")
