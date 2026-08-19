# .............................transfer sattements....................

# 1.sum of given numbers
# numbers = [25,30,20,40,15,25]
# sum=0
# for i in numbers:
#     sum = sum + i
#     if sum > 100:
#         break
# print(f"last iteration {i}")
# print(f"sum, {sum}")
# print(f"sum exceeded 100,{sum})

# 2. odd numbers
# for i in range(1,601):
#     if i%2 !=0:
#         continue
#     print(i)

# 3.odd even check 
# number = int(input("enter a number:"))
# if number %2 ==0:
#     print('even')
# else:
#     pass 

# 4. combining transfer statements.
# words = ['nani','nithin','nuthan','ravi','raghu','ramesh','vijay','govardhan']

# for i in words:
#     if i == 'nithin':
#         break
#     elif i =='raghu':
#         continue
#     print(i)

# 5.
#  list1 = ['hi', 'hello', 'welcome']
# names = ['nuthan', 'nithin','james', 'nikhil']
# for items in list1:
#     for name in names:
#         print(items, name)
#         if items == 'hello' and name == 'nithin':
#             break
#     print("out for inner loop")
# print("out from loop")

# ...........................................list................................  
# 1.
# my_list = [10,20,30,40,50,11]
# for i in my_list[::-1]:
#     print(i)

# my_list = [10,20,30,40,50,60,11]
# my_list.reverse()
# print(my_list)

# 2.
list3 = []
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print(list3)   
        #  or

result = [i for i in list1 for j in list2 if i == j]    
print(result)    

# 3.unique elemnts 
# numbers = [1,2,2,3,4,5,4,11,23,44,22,11,11,11,11,6]
# unique_list = []

# for i in numbers:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)  

# -------------or-----------
# result = [i for i in numbers if i not in unique_list]     
# print(result)  

# 3.remove duplicates
# duplicated_list =[1,2,3,2,3,4,5,32,3,2,3,4,5]
# duplicated_list.set
# print(duplicated_list)

# 4. remove duplicates:
# duplicated_list = [1,2,2,3,4,4,5]
# empty_list = []
# for i in duplicated_list:
#     if i!= 2 and i!= 4:
#         empty_list.append(i)
# print(empty_list)        

# result = [i for i in duplicated_list if i!=2 and i!=4]
# print(result)

# 5.list concatenation
# name1 = ['nithin']
# name2= ['nuthan']
# print(name1+name2)

# 6.list repetation
# list1 = [1,2,3,4,4,4,4,4,4,4,4,45,6,'nithin','nuthan',9,0]
# print(list1.count(4))

# 7.list removal
# num = [1,2,3,4,5,6,7,8,9]
# num.remove(9)
# print(num)

# 8.list insertion
# num = [1,2,3,4,5,6,7,8,9]
# num.insert(0,10)
# num.insert(1,11)
# num.insert(2,12)

# print(num)

# ................................list comprehensions............
# 1.square numbers
# square_numbers = [i**2 for i in range(1,11) ]
# print(square_numbers)

# 2.even numbers
# even_num = [i for i in range(1,11) if i%2==0]
# print(even_num)

# 3.words lengths
# words = ['mango','orange','sapota','pine']
# print(len(words))