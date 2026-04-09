RATE = 5
balance = 10000
target = 20000
year = 0

while balance <= target :
    year = year +1
    interest = balance * RATE/100
    balance = balance + interest
    print(year , balance)
