grades = []
for i in range(5):
    grade = float(input("enter a grade: "))
    grades.append(grade)
print(grades)

for grade in range(len(grades)):
    print(grades[grade])
    
for i in grades:
    print(i)
    