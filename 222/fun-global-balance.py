balance = 1000
def withdraw(amount):
    global balance     #this function to reach the global function (balance), wich is defined before.
    if balance >= amount:
        balance = balance - amount
        
withdraw(350)
print("balance: " , balance)