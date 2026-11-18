#Extract full name from the txt file created
file = open("fullname.txt", "r")
fullname = file.read()
file.close()
print(fullname)
my_names = fullname.split()
print(my_names)
first_name = my_names[0]
middle_name = my_names[1]
last_name = my_names[2]
print("First Name: ", first_name)
print("Middle Name: ", middle_name)
print("Last Name: ", last_name)

#Extract current directory path
import os
path = os.getcwd()
print("Current Directory Path: ", path)

#Open and read the HTML file
file = open("baby2008.html", "r")
values = file.read()
file.close()
#Extraction using regex
import re
pattern = r'<td>\d+</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>'
matches = re.findall(pattern, values)
print("Extracted Names: ", matches[:5])
names = []
for boy, girl in matches:
    names.append(boy)
    names.append(girl)
print(names[:5])

#Sort the names in alphabetical order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_names = bubble_sort(names)
print("Sorted Names: ", sorted_names[:20])

#Binary search function to find a name in the sorted list
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search(sorted_names, "Emily")
if result != -1:
    print("Found at:", result)
else:
    print("Name not found")