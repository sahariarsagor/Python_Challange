n = int(input("Enter terms: "))

# initial value set 
a = 0
b = 1

for i in range(n):
    # print the value of a which store current fibonacci 
    print(a, end=" ")
    a, b = b, a + b 

""" 
    line explaining a, b = b, a+b
    this line mean:
        a = b
        b = a+b
    but its work first calculate right side like: b, a+b
    then assign value same time. 
"""