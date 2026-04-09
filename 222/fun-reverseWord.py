def  reverse_word(word):
   reverse = ""
   for i in range(len(word)-1,-1,-1):
       reverse = reverse + word[i]
   return reverse
print(reverse_word("khadija"))


      
      
    