#finde the max in the list
values = [2,5,3,4]
v = values[0]
for i in values:
    if v < i:
        v = i
print(v)


# find the min in the list
values = [2,5,3,4]
v = values[0]
for i in values:
    if v > i:
        v = i
print(v)

