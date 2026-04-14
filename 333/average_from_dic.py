bigdic = {
    "Ali": {"Math": 85, "Science": 78, "English": 92},
    "Sara": {"Math": 90, "Science": 88, "English": 85}
}


math_total = 0
scince_total = 0
english_total = 0
count = 0

for name in bigdic:
    math_total += bigdic[name]["Math"]
    scince_total += bigdic[name]["Science"]
    english_total += bigdic[name]["English"]
    count +=1
    
print("math Average=" ,math_total / count )
print("science Average =", scince_total/ count)
print("english_Average =", english_total/ count)
