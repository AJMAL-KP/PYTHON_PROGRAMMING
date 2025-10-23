def fact(a):
    if a < 0:
        return "Factorial not defined for negative numbers"
    elif a==0:
        return 1
    else:
        return a*fact(a-1)
    

a=int(input("enter a number"))

print(fact(a))