num = 2
while num < 200:
    
    counter = 2
    isprime = True
    while counter < num:
        if num % counter == 0:
           isprime = False
        counter =  counter + 1
    
    if isprime:
         print("the num is prime" , num)
    num = num + 1
     
