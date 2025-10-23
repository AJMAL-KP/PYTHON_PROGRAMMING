
def pattern(sym, limit):
    for i in range(limit):
      
        for j in range(limit - (i + 1)):
            print(" ", end="")  
        
        for k in range(i + 1):
            print(sym, end="")
        
        print()


sym = input("Enter the symbol: ")
limit = int(input("Enter the limit: "))


pattern(sym, limit)
