x=input("enter three numbers : ").split()
if int(x[0])>=int(x[1]):
    if int(x[0])>=int(x[2]):
        print(int(x[0]))
    else:
        print(int(x[2]))
else:
    if int(x[1])>=int(x[2]):
        print(int(x[1]))
    else:
        print(int(x[2]))