def calculation(a,b):
   summ = a + b
   return summ

res = calculation(40,10)
print(res)


#####
def func1(a,b):
    def func2():
        return a + b
    return func2() + 5
print(func1(2,5))