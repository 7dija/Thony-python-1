records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]


bigdic = {}
for name,subject , mark in records:
    if name not in bigdic:
        bigdic[name] = {}
    
    bigdic[name][subject] = mark
    
print(bigdic)


        
        

    
    