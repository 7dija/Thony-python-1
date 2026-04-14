contacts = {"fred":[111,444] , "mary":222,"Bob":333}
for item in contacts.items():
    print(item[0] , item[1])
    
    if type(item[1]) is list:
        for i in item[1]:
            print(i)
            