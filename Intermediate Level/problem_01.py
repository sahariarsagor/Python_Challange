# Find the second largest element in list. 

#here is our list 
myList = [10, 20, 28, 5, 8, 11, 27, 10, 11]

#removing duplicate elements in list
uniqueList = list(set(myList))
#sorting our unique list
uniqueList.sort()

# checking something: 
if len(uniqueList) < 2:
    print("not enough unique element left")
else:
    secondLargest = uniqueList[-2]
    print("Second largest element is: ", secondLargest)