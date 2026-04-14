dictionary = {"fred":[111,444] , "mary":222,"Bob":333}
for key in dictionary:
    if type(dictionary[key]) is list:
        count = 0
        for i in dictionary[key]:
            count += 1
            print(key,i, "" ,count)
        
    else:
        print(key,dictionary[key])
    