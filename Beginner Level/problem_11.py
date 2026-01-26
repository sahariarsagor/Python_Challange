# check is this number is armstrong or not 

"""
    Decoding problem 11
    
    armstrong mean 
    if a number n = 125
    size of n = 3
    sum = 1**3 + 2**3 + 5**3
    if sum == n then its a armstrong number 
"""
# get number from user 
n = int(input("Enter a number: "))

# initial sum value set and find the size of number 
sum = 0
digit = len(str(n))

# calculate sum using for loop 
for d in str(n):
    temp = int(d) #convert type of d 
    p = temp ** digit #calculate the power value
    sum += p # final sum calculation 

# checking is this number is equal to sum 

if int(n) == sum:
    print("Given number is an armstrong number ")
else:
    print("Given number is not an armstrong number")