# find factorial of a number 
# Factorial rulse:  3! = 1 X 2 X 3 


# This is way to use recursion to find factorial 
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# print("Factorial of", num, "is", factorial(num))


num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num+1):
    factorial *= i 

print("The factorial of ", num, "is: ", factorial)