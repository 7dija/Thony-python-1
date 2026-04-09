def Fibonacci_Number(num):
    a = 0
    b = 1
    print(a)
    for i in range(num+1):
        temp = a
        a = b
        b = b + temp
       
        if a > num+1:
            break
        else:
            print(a)


Fibonacci_Number(10)
        
        
    
   
    
        
    
    
    