prev = ""
while True:
    num = input("write a number or ENTER to exit: ")
    
    if num == "":
        break
    if num == prev:
        print("the adjecent number is: " , num)
        
    prev = num
    
    