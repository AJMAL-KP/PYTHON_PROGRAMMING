word=input("Enter a word")
list1=[]

for i in word:
    if i in "aeiouAEIOU" :
        list1.append(i)

print(list1)