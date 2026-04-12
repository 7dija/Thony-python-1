num =[5,9,6,8,3,10]
index = -1
number = int(input("enter a number"))
for i in range(len(num)):
    if num[i] == number:
        index = i
        # use break to stop the process when first value founded
        break  
print(index)
    


