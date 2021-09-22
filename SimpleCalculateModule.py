print('You are welcome in this module which is a simply calculate for numbers')

while True:
    try:
        a = int(input('Please enter first number: '))
        b = int(input('Please enter second number: '))
        if (a,b) == True:
            method()
    except ValueError:
        print("Not an integer!")
        break

    o = input("What operation you want to do, sum '+', substraction '-' , multipy '*' or split '/': ")
    if o == '+':
        print('The score is: ', a + b)
    elif o == '-':
        print('The score is: ', a - b)
    elif o == '*':
        print('The score is: ', a * b)
    elif o == '/':
        if b == 0:
            print('You cannot split by 0!')
        else:
            print('The score is: ', a / b)
    else:
        print('Function does not contain your choice')
