dic ={
    "sunday" : [30, 29],
    "monday" : [29,31],
    "tuesday" : [31,32],
    "wednisday" : [33,34],
    " thursday" : [35,29],
    "friday" : [28,35],
     "saterday" : [25,33]
    }

index = 0
week3 = [ 30, 28,35,29,28,35,32]
for key in dic.keys():
    dic[key].append(week3[index])
    index += 1
print(dic)



##---------------------------------------other way
# for key in dic.key:
#     user_input = int(input("enter temp for" , key , "week3"))
#     duc[key].append(user_input)









