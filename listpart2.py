# 1) Write Python code to reverse the order of elements in the given list Print the reversed list

my_list = [10, 20, 30, 40, 50, 11]
print(my_list[::-1])
print(my_list[5::-1])

# 2) Given two lists list1 and list2 , find and print the common elements between them

emptylist = []
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for i in list1:
    if i in list2:
        emptylist.append(i)
print(emptylist)

# 3) Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list

empty_list = []
original_list = [1, 2, 2, 3, 4, 4, 5]

for i in original_list:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)

# 4) Remove duplicate elements from the given list duplicated_list and print the list without duplicates while preserving the order.

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
emptylist = []
for i in duplicated_list:
    if i not in emptylist:
        emptylist.append(i)
print(emptylist)

# 5) Write a Python script that concatenates two lists and prints the result

list1 = [12, 34, 56, 78, 90, 2, 13]
list2 = [24, 35, 46, 57, 68, 79, 80]
result = list1 + list2
print(result)

# 6) Write a Python script that repeats a list three times and prints the result

list = [31, 53, 36, 22]
print(list*3)

# 7) Write a Python script that removes the elements at even indices from a list

list = [13, 22, 56, 73, 48, 45, 34]
print(list[0::2])

# 8) Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list

list = [23, 2, 45, 5, 78, 9]
list.insert(0, 12)
list.insert(0, 11)
list.insert(0, 10)
print(list)

# 9) (1) Square Numbers: Create a list of squares of numbers from 1 to 10

empty_list = []
for i in range(1, 10):
    n = i**2
    empty_list.append(n)
print(empty_list)

# 10) (2)  Even Numbers: Generate a list of even numbers from 1 to 20

empty_list = []
for i in range(1, 20):
    if i % 2 == 0:
        empty_list.append(i)
print(empty_list)

# 11) (3) Words Lengthsî‚’ Given a list of words, create a list containing the lengths of each word

words = ["apple", "banana", "cherry", "date"]
empty_list = []
for i in words:
    i = len(i)
    empty_list.append(i)
print(empty_list)
result = [len(i) for i in words]
print(result)