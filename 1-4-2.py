from sys import exit

mark = float(input("enter the mark: "))

if mark < 0 or mark > 100:
    exit("Error: enter a value betwen 0 and 100 ")

if mark >= 90:
    print("A grade")
elif mark >= 80:
    print("B grade")
elif mark >=70:
    print(" C grade")
else:
    print("F grade")