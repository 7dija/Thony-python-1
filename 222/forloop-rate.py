RATE = 5
initial_balance = 10000

year_num = int(input("enter number f years"))

balance = initial_balance
for year in range(1, year_num + 1):
    interest = balance * RATE / 100
    balance = balance + interest
    print(year , balance)
    