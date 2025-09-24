x=int(input("enter first number:\n"))
y=int(input("enter second number:\n"))
while(1):

    op=int(input("Select operation:\n 1. +\n 2. -\n 3.*\n 4. /\n 5. Exit\n"))
    if op==1:
        print(x+y)
    elif op==2:
        print(x-y)
    elif op==3:
        print(x*y)
    elif op==4:
        print(x/y)
    else:
       break