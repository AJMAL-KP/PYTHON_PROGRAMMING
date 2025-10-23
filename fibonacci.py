# def fibo(a):
#     a,b=0,1
#     for i in range(c+1):
#         print(a,end=' ')


# c=int(input(("how many numbers to be considered")))
# fibo(c)




def fibonacci(a):
    if a<= 1:
        return a
    
    return fibonacci(a-1)+fibonacci(a-2)

for i in range(int(input("Enter a num:"))):
    print(fibonacci(i), end=" ")


