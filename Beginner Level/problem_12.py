import math 

# writting the prime number logic 

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n%i == 0:
            return False
    return True

for i in range(101):
    if isPrime(i):
        print(i, end=" ")
        

