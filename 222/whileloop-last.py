num = input("enter a number")
count = 0

while count < len(num):
    if int(num[count]) % 2 == 0:
        print(int(num[count]))
    count = count + 1
        
        
        