x = int(input("Enter number: "))

if x < 0:
    print("Factorial is not defined for negative numbers.")
elif x == 0:
    print("Factorial of 0 is 1")
else:
    fact = x
    while x >= 2:
        fact *= x - 1
        x -= 1
    print(fact)
