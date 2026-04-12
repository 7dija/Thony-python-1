List = [1,2,3,4,5]
target = 6

for value in range(len(List)):
    
    for i in range(value+1,len(List)):
        if List[i] + value == target and List[i] != value:
            print(List[i] , List[value-1])

            


