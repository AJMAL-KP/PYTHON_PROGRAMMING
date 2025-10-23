a, b = map(int,input("Enter two numbers separated by space: ").split())
while b>0:
    a,b=b,a%b

print("gcd:",a)