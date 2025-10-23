def add(str):
    str=str.lower()
    if str[-3:] == "ing":
        str+="ly"
    else:
        str+="ing"
    return str



    
str=input("Enter a string: ")
result=add(str)
print(result)

