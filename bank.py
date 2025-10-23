class Account:
    def __init__(self,name,acc_no,acc_type,balance):
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.balance=balance
    
    def display(self):
        print("Name: ",self.name,"Account No: ",self.acc_no,"Account tye: ",self.acc_type,"balance: ",self.balance)
    
    def deposit(self,amount):
        self.balance+=amount
        print(amount," deposited")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough balanace")
            return
        else:
            self.balance-=amount
            print(amount," withdrawed")

name=input("Enter name: ")
acc_no=int(input("Enter account number"))
acc_type=input("Enter the type of account")
member=Account(name,acc_no,acc_type,0)
while(1):
    member.display()
    transaction=int(input("Enter 1 to deposit and 2 to withdraw"))
    if transaction==1:
        member.deposit(int(input("Enter the amount to deposit")))
    elif transaction==2:
        member.withdraw(int(input("Enter the number to be withdrawed")))
    else:
        print("Invalid")