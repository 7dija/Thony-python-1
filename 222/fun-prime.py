def primenum(num):
 count = 2
 isprime = True
 while num > 0:
     if num % count == 0:
      isprime = False
     count =  count + 1
     return isprime
print(primenum(7))

     
    
    
         
    
    