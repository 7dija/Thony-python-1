def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n* factorial(n-1)
print(factorial(5))

#######

def sumfunc(n):
    if n == 0:
        return 0
    return n+ sumfunc(n-1)

print(sumfunc(10))   