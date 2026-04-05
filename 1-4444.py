major = input("enter your major: ").lower()
major = input("enter your major: ").find("eng")
gender = input("enter your gender: ").lower()
gender = input("enter your gender: ").find("f")

if major == "engineering":
  if gender == "female":
      print("the student major is Engineering, and she is a girl")
  else:
      print("the student major is no Engineering, and she is not a girl")

else:
    print("the major is not Engineer , and not Female")

