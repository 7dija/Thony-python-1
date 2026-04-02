hour1 = int(input("enter the first hour: "))
min1 = int(input("enter thr first minute: "))

hour2 = int(input("enter the second hour: "))
min2 = int(input("enter thr second minute: "))

if hour1 > hour2 and min1 >= min2:
    print("time one comes first")
elif hour1 > hour2 and min1 <= min2:
     print("time one comes first")
elif hour1 == hour2 and min1 > min2: 
    print("time one comes first")

elif hour1 < hour2 and min1 <= min2:
     print("time two comes first")
elif hour1 < hour2 and min1 >= min2:
     print("time two comes first")
elif hour1 == hour2 and min1 < min2:
     print("time two comes first")

else:
    print("Time 1 = Time 2")