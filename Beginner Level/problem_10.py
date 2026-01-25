# problem 10
# count the digit of a number 

n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count += 1

print("Numebr of digit is: ", count)