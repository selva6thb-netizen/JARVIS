class student:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print("Name:",self.name)
        print("Balance:",self.balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance.")
        else:
            self.balance-=amount
    def balance_inquiry(self):
        print("Current balance:",self.balance)
selva=student("Selva",1000)
name=input("enter name: ")
print(name)
action=int(input("enter action: 1.Deposit 2.Withdraw 3.Balance Inquiry: "))
if action==1:
    amount=int(input("enter deposit amount: "))
    selva.deposit(amount)
    print("Deposit successful.\n current balance:",selva.balance)
elif action==2:
    amount=int(input("enter withdrawal amount: "))
    selva.withdraw(amount)
    print("Withdrawal successful.\n current balance:",selva.balance)
elif action==3:
    selva.balance_inquiry()
else:
    print("Invalid action.")