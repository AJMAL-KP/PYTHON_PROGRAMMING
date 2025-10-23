def frequency(string, char):
    count=0
    for i in range(len(string)):
        if string[i]==char:
            count+=1
    return count

string=input("Enter a String:")
freq = {x: frequency(string, x) for x in string}
print(freq)