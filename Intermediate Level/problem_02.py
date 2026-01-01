# find the duplicate in a list 

myList = [10, 11, 5, 8, 5, 2, 10, 5, 2, 8, 11, 5]

seen = []
duplicate = []

for n in myList:
    if n in seen:
        if n not in duplicate:
            duplicate.append(n)
    else:
        seen.append(n)

print("Duplicate found: ", duplicate)        