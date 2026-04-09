num1 = int(input("enter a value: "))
count = 0
while num1 != "" :
    value = int(num1)
    if value < 0:
        count = count + 1
    num1 = input("enter a value: ")
    
print("count of negative value is:" ,count)
        
       
    



         
    