# x=[]
# y=[]
# x=map(int,input("Enter numbers").split())

# for i in x:
#     if i>0:
#         y.append(i)
# print(y)

x=[]
y=[]
x=input("Enter numbers").split()

for i in x:
    if int(i)>0:
        y.append(int(i))
print(y)