infile = open("C:/Users/DELL/Desktop/paragraph.txt" , "r")

text = infile.read()
wordlist = text.split()

print("the words: " ,wordlist)
print("the count of words: " ,len(wordlist))

#--------------------------------------------------------
rep = 0
for i in range(len(wordlist)):
    if wordlist[i].lower().strip() == "the":
        rep = rep + 1

print(rep)
#-------------------------------------------------------
#to finf the indexes of the
theIndex = []
for i in range(len(wordlist)):
    if wordlist[i] == "the":
        theIndex.append(i)
#---------------------------------------------------------
#TO SAPERATE THE PARAGRAPH BY "THE"
for index in range(len(theIndex)):
    if index == len(theIndex)-1:
        print(wordlist[theIndex[index]: ])
    else:
        print(wordlist[theIndex[index]: theIndex[index+1]])
        







infile.close()