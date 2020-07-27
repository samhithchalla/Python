#Calculator Program

print("Welcome to Python Calculator")
ext = 1
while ext==1:
    n1 = int(input("\nEnter 1st number: "))
    n2 = int(input("Enter 2nd number: "))

    addition = n1+n2
    subtraction = n1-n2
    multiplication = n1*n2
    division = n1/n2

    opr = input("Enter the operation you want to perform (add/sub/mul/div): ")

    if opr == 'add':
        result = addition
    elif opr == 'sub':
        result = subtraction
    elif opr == 'mul':
        result = multiplication
    elif opr == 'div':
        result = division

    print("Result is: ",result)

    code = input("\nWant to exit Calculator(y/n): ")
    if code=='y':
        print("Thank you")
        ext=0
    elif code=='n':
        ext=1
exit(0)