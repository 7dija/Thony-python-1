dic ={
    "sunday" : [30, 29],
    "monday" : [29,31],
    "tuesday" : [31,32],
    "wednisday" : [33,34],
    " thursday" : [35,29],
    "friday" : [28,35],
     "saterday" : [25,33]
    }


# for day , temps in dic.items():  #to print them all use (day,temps). to print keys of first week use(day, temps[0]). and(day,temps[1]) for second week
#     print(day , temps[1])


count = 0
totalTemp = 0
for day1 , temps1 in dic.items():
    totalTemp += temps1[1]
    count += 1
average = totalTemp / count
print(average)

