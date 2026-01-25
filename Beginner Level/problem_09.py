# problem 09 
# check is this number is palindrome or not 

n = int(input("Enter a number to check: "))

original = n
reverse = 0

while n > 0:
    Lastdigit = n%10
    reverse = reverse*10 + Lastdigit
    n = n // 10

if reverse == original:
    print("Given number is a palindrome number")
else:
    print("Given number is not palindrome number")