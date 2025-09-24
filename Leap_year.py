from datetime import datetime 
x=datetime.now().year
y=int(input("ENter ending year"))

for i in range(x,y+1):

    if (i%4 ==0 and i%100 !=0 ) or (i%400 == 0) :
   
        print(i)
    

