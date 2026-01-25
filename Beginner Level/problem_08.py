# problem 
# write a python program to reverse a number 

n = int(input("Enter a number: "))
r = 0

while n > 0:
    d = n % 10 #store remember 
    r = r * 10 + d # setting reverse value 
    n = n // 10 # decrease the value of n 

print(f"reverse value of this number is: {r}")