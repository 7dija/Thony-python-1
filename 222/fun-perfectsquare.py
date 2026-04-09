def perfecrsqr(num):
    import math
    result = math.sqrt(num)
    if result.is_integer():
        return result
    else:
        return "not a perfect sqrt"
    
print(perfecrsqr(3))
     

 
    

