amount = 500
balance = 200

if amount > balance:
    raise ValueError("amount acceded balance")
#-------------------------------------------------

try:
    infile = open("input.txt" , "r" )
    
    line = infile.readline()
    print(line)
    
except IOError:
    print("could not open input file. ")
except Exception as exceptObj:
    print("Error" , str(exception))
#------------------------------------------------
 try:
    infile = open("input.txt" , "r" )
    
    line = infile.readline()
    print(0/5)
    print(line)
    
except IOError:
    print("could not open input file. ")
except Exception as exceptObj:
    print("Error" , str(exception))
#------------------------------------------------
inputOK = False
while (inputOK == False):
    try:
        num = input("Enter a number: ")
        num = float(num)
        inputOK = True
    except ValueError:
        print("non numerecal num enterde '%s' " %num)

num = num * 2
print(num) 