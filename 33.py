number = float(input("enter how much did you pay: "))
if number >= 128 :
    priceDiscount = number-(92/100*number)
    print("the price after discount is:" ,priceDiscount)
else:
    priceDiscount = number-(84/100*number)
    print("the price after discount is:" ,priceDiscount)
    
    