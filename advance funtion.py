#syntax
# lamda arguments: expression 

# def add(a,b):
#     return a+b
# obj=add(10,10)
# print(obj)

# result = lambda a,b: a+b
# print(result(10,20))


#filter--> filter(function,iterable)

# list_1=[23,4,5,4,542,232,3,53,5,646,4667,57,68,4,3,24,45,6]
# empty_list=[]
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# def even(a):
#     return a%2==0
# obj=even(24)
# print(obj)


# list_1=[1,2,32,32,3,4,34,34,34,45,4,576]
# def even(a):
#     return a%2==0
# result=filter(even,list_1)
# print(list(result))

# list_1=[1,2,32,32,3,4,34,34,34,45,4,576]
# result=filter(lambda a:a%2==0, list_1)
# print(list(result))

# def squares(a):
#     return a**2
# result = map(squares,list_1)
# print(list(result))

# list_1=[1,2,32,32,3,4,34,34,34,45,4,576]
# list_2=[3,4,5,67,8,9,0,4,32,5,667,7,8]
# result=map(lambda a,b : a**b, list_1,list_2)
# print(list(result))


# from functools import reduce

# list_1=[1,2,32,32,3,4,34,34,34,45,4,576]
# def add(a,b):
#     return a+b
# result=reduce(add,list_1)
# print(result)

# list_1=[1,2,32,32,3,4,34,34,34,45,4,576]
# result=reduce(lambda a,b : a/b, list_1)
# print(result)

# list_3=[1,2,3,3,2,2,3,34,4,4,4,5,5]

# result=map(lambda a: a**2,list_3)
# print(list(result))


# List_4=(-2,-3,4,4,5, 676,3,4,66,67,-4,-6,-7,-9)

# result=filter(lambda a: a>=0,List_4)
# print(list(result))

from functools import reduce
# list_5=[2,2,32,3,4,3,435,534,5345,64,]
# result=reduce(lambda a,b:a*b, list_5)
# print(result)

string="today it feels very exsiting because i am learing python next level"
vovels="AEIOUaeiou"
result=reduce(lambda a,b: a+[b] if b in vovels else a, string,[])

print(len(result))


