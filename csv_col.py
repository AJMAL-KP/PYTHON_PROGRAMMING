import csv

with open(input("File: "), "r") as file:
    reader = csv.reader(file)
    
    # For Extracting the field names line by line
    fields = next(reader)
    choice = int(input("Enter the column to print: "))
    
    col = []
    for row in reader:
        col.append(row[choice])
    print(fields[choice], "\n", col)