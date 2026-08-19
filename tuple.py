# tuple_1 = ()
# print(tuple_1)
# print(type(tuple_1))


# tuple_2 = (1,5.7,True,"pythonlife",[1,2,3],(1,2,3),25,25,25,25)
# print(tuple_2)
# print(type(tuple_2))


# tuple_3 = tuple()
# print(tuple_3)
# print(type(tuple_3))



# a = 1
# print(a)

# a=b=c=d = 1
# print(a)
# print(b)
# print(c)
# print(d)


# a,b,c,d, = 1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)


a = 1,5.7,"pythonlife",True
print(a)




# a = 10
# b = 20

# a,b = b,a
# print(a)
# print(b)


# sample = (5,"pythonlife",True,[1,2,3,4],5.7)
# print(len(sample))
# print(sample.count("nithin"))




# sample = (5,"pythonlife",True,[1,2,3,4],5.7)
# print(sample.index("pythonlife"))

# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# result_tuple = tuple1 + tuple2
# print(result_tuple)
# print(result_tuple*3)


# fruits = ('guava', 'pine', 'grapes')
# is_grapes_present = 'grapes' in fruits
# print(is_grapes_present)

# sample = ()
# print(all(sample))



# Item		Price
# --------------------
# pine		99.00
# grapes	99.00
# guava		49.00
# --------------------
# Total		247.00


# items = [("pine", 99), ("grapes", 99), ("guava", 49)]
# print(f"Item\tPrice")
# print("-"*25)
# sum = 0
# for i,j in items:
#     print(f"{i}\t{j}")
#     sum += j #eq--> sum = sum + j ( price )
# print("-"*25)
# print(f"Total\t{sum}")


print(25 * "=", "Pythonlife Supermarket", 25 * "=")
print(28 * " ", "Hyderabad")
print("Name:", "nithin", 30 * " ","August 04 2026")
print(75 * "-")
print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')