x=int(input("Enter the number\n"))
y=int(input("enter the number of multiples you want: "))
print(f"{y} multiples of {x} are :")

for i in range(1,y+1):
    print(f"{i}x{x}={i*x}")