values = [1,3,1,4,5,3,1]
d = []
for value in range(len(values)):
    if values[value] not in d:
        count = 1
        for i in range(value+1,len(values)):
            if values[i] == values[value]:
                count += 1
        if count >= 1:
            dic = ({values[value] : count})
            

        
        d.append(values[value])
        print(dic)


 