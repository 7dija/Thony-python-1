username = input("enter your username: ")
passwoord = input("enter your password: ")
               
if username == "admin" and passwoord == "1234" or username == "guest":
               print("Access garanted")
else:
    print("you are not the admin")
               