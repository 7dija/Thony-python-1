grade = 0
total = 0
count = 0
while grade >= 0:
    grade = float(input("enter a grade or -1 to finish"))
    if grade >= 0:
        total = total + grade
        count = count + 1 
Avareg = total / count
print(Avareg)


    
    