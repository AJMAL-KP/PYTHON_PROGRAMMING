import math

a=float(input("Enter a: \n"))
b=float(input("Enter b: \n"))
c=float(input("Enter c: \n"))


dis=b**2-4*a*c

if dis>0:
    root1=(-b+math.sqrt(dis))/2*a
    root2=(-b-math.sqrt(dis))/2*a
    print(f"real and different roots: {root1} , {root2}")
elif dis==0:
    root1=-b/(2*a)
    print(f"real and same root: {root1}")
else:
    real_part=-b/(2*a)
    img_part=math.sqrt(abs(dis))/2*a
    print(f"The roots are complex: {real_part}+{img_part}i and {real_part}-{img_part}i")