count = 0
num = input("enter a number")
total = 0

while count < len(num):
    total = total + int(num[count])
    count = count + 1
print(total)
