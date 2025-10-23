li=list(map(int,input("enter list seperated by space").split()))
print("before removing even numbers",li)
li = [i for i in li if i % 2 != 0]
print("after removing even numbers",li)