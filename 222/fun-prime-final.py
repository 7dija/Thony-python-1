def prime(num):
    count = 2
    while count < num:
        if num % count  == 0:
            return False
        count +=1
    return True
print(prime(9))