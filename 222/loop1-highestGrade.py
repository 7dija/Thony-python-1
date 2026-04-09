grade1 = 0
highest_grade = 0
while grade1 >= 0 :
    grade1 = float(input("enter a grade or -1 to finish"))

    if highest_grade <= grade1:
        highest_grade = grade1
         
print("highest grade is: " ,highest_grade)
         
    
    
