def multiply(lis, factor):
    lis = list(lis) #coby by value , without it it will be by refrens so the orignal list will iffect
    for i in range(len(lis)):
        lis[i] = lis[i] * factor
    return lis
listt = [1,2,3,4]
factor = 2
print(multiply(listt , factor))
print(listt)