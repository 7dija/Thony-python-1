vawels = 0
word = "khadja"
vowels = 0
for char in word:
    if char.lower() in "aeiou" :
        vowels = vowels + 1
print(vowels)
