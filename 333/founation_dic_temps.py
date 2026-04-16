dic ={
    "sunday" : 30 ,
    "monday" : 29,
    "tuesday" : 31,
    "wednisday" : 33,
    " thursday" : 35,
    "friday" : 28,
     "saterday" : 25
    }
print(len(dic))  #to know number of items

for key in dic:
    print(key , dic[key]) #to print each key with its value
    
print(sum(dic.values())) # to calculate the sum of vaues,  and "values" here is constante
# print(max(dic.values())) 
# print(min(dic.values()))


maxmm = 0
for value in dic.values():
    if value > maxmm:
        maxmm = value
        
for item in dic.items():  #i use items insted of values because i need key and value poth
    print(item[0],item[1])
    if item[1] == max:
        print("this max temp was on day: ", item[0])