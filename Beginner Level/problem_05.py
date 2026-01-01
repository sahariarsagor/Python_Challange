# check prime number 

import math

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

# checking a number 
n = int(input("Enter a number: "))

if isPrime(n):
    print(f" given {n} is a prime number")
else:
    print(f"given {n} is not a prime number")