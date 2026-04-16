infile = open("C:/Users/DELL/Desktop/data.txt" , "r")

line = infile.readline()
nolines = 0
while line != "":
    print(line)
    nolines += 0
    line = infile.readline()
infile.close()

#--------------------------------------------

infile = open("C:/Users/DELL/Desktop/data.txt" , "r")

line = infile.readlines()
print(line)    
infile.close()

# ------------------------------------------------
infile = open("C:/Users/DELL/Desktop/data.txt" , "r")

lines = infile.readlines()


for line in range(len(lines)):
    
    lines[line] = lines[line].strip()
print(lines)

infile.close()
#-------------------------------------------------
infile = open("C:/Users/DELL/Desktop/data.txt" , "r")

lines= infile.read().split("\n")

infile.close()

#-------------------------------------------------
infile = open("C:/Users/DELL/Desktop/data.txt" , "w")


#infile.write("HELLO\nIT IS ME")
#or

print("HI EVERY ONE" ,end = "", file= infile)

infile.close()


