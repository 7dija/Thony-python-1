amount = 1000
user_name = "khadija"
paswoord = "123"

while True:
      user_name1 = str(input("enter your name"))
      paswoord1 = input("enter your paswoord")
     
      if user_name1 == user_name and paswoord1 == paswoord:
           print("select : 1 for check balance, 2 for diposit mony, 3 for withdraw mony ")
           option = input("   ")
           if option == "1":
               print("your balanse is:" ,amount)
           elif option == "2":
               A1 = int(input("how much you diposit?: "))
               print("your balanse now is: " ,amount + A1)
        
           elif option == "3":
               A2 = int(input("how much you withdraw?: "))
               print("your balanse now is: " ,amount - A2)


        
                        
else:
    print("access denaid")