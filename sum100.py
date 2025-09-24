sum=0
count=0
num=1
while(count<100):
    if num%2==0:
        sum+=num
        num+=1
        count+=1
    else :
        num=num+1
print(sum)