values = [2,3,4,5,6,7]
target = 6
first = 0
last = len(values)-1
isfound = False
while first <= last:
    mid_value =(first + last)//2
    
    if values[mid_value] == target:
        print("target founded at endex " , mid_value)
        isfound = True
        break
  
    elif target > values[mid_value]:
        first = mid_value + 1
        
   
    else:
        last = mid_value - 1
        
if not isfound:
    print("target not in the list")