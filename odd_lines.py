f=open("file1.txt","r")
s=open("file2.txt","w")
lines=f.readlines()
print(len(lines))
for i in range(1,(len(lines))+1):
    if i%2!=0:
        s.write(lines[i-1])

f.close()
s.close()


