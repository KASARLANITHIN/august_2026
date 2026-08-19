# Sets:
# #Union of two sets: Aug:3_2026
# Set_1 = {1,2,3,4,5,6,7,8,9,10}
# Set_2 = {5,6,7,8,9,10,11,12,13,14,15}   
# Set_3 = Set_1.union(Set_2)
# print(f"Union of Set_1 and Set_2: {Set_3}") # Print the unique elements

# #Intersection of two sets: Aug:3_2026
# Set_1 = {1,2,3,4,5,6,7,8,9,10}
# Set_2 = {5,6,7,8,9,10,11,12,13,14,15}
# Set_3 = Set_1.intersection(Set_2)   
# print(f"Intersection of Set_1 and Set_2: {Set_3}") # Print the common elements

# #Symmetric_difference:
# Set_1 = {1,2,3,4,5,6,7,8,9,10}
# Set_2 = {5,6,7,8,9,10,11,12,13,14,15}
# Set_3 = Set_1.difference(Set_2)
# print(f"Difference of Set_1 and Set_2: {Set_3}") # Print the elements that are in either set but not in both

# #Difference of two sets:
# Set_1 = {1,2,3,4,5,6,7,8,9,10}
# Set_2 = {5,6,7,8,9,10,11,12,13,14,15}
# Set_3 = Set_2.difference(Set_1)
# print(f"Difference of Set_2 and Set_1: {Set_3}") #Display the set_2 elements here

# #Disjoint sets:
# Set_1 = {1,2,3,4,5,6,7,8,9,10}
# Set_2 = {11,12,13,14,15}    
# Set_3 = Set_1.isdisjoint(Set_2)
#print(f"Are Set_1 and Set_2 disjoint sets? {Set_3}") #Display True or False 

#Superset
# Set_1 = {1,2,3,4,5,6}
# Set_2 = {1,2,3,4,5}    
# Set_3 = Set_1.issuperset(Set_2)
# Set_4 = Set_2.issubset(Set_1)
# print(f"Set_1 is superset of Set_2: {Set_3}") #If Set_2 contains what elements having from Set_1 then it will returns True else returns false
# print(f"Set_2 is subset of Set_1: {Set_4}") # Subset

# Voter_list_1 = {"nithin","viju","harsha","raghu"}
# Voter_list_2 = {"nithin","viju","harsha","raghu","nuthan","jashu"}    
# print(Voter_list_1.issuperset(Voter_list_2)) # It is not so returns False
# print(Voter_list_2.issubset(Voter_list_1)) # It is not so returns False

#Frozen set: It is a function frozenset() which creates an immutable frozen set object
# Set_1 = {1,2,3,4}
# #Set_1.add("Python")
# print(Set_1)

# #Now making as a frozen set
# Set_2 = frozenset(Set_1)
# print(Set_2)
# #Now try to add an element to the frozen set
# Set_2.add("Python")
# print(Set_2)
# We cannot modif but we can perform above mentoned operations


#Tuples:
# Tuples are a kind of data structures which is similar to lists
# Difference is list can be changed once it got created where as tuples cannot be changed once got created

# Tuple_1 = ()
# print(type(Tuple_1))
# print(Tuple_1)

# tuple_2 = (1,2,3,4,5,3,4,5,"python",[1,2,3],[4,5,6]) #Can perform indexing, slicing since it is ordered collection of elements
# print(type(tuple_2))
# print(tuple_2)   

# a= 1
# print(a)

# a =b =c = 1
# print(a,)
# print(b)
# print(c)

# a,b,c,d = 1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)

# a = 1,2,3,"python",[1,2,3]
# print(a)

# #How to swap with out using 3rd variable
# a =10
# b =20
# a,b = b,a
# print(a)
# print(b)

# We can swap using arithmetic operation as well

# Sample_tuple = (1,2,3,4,5,[1,2,3],"python")
# print(len(Sample_tuple))

# Sample_tuple = (1,2,3,4,5,[1,2,3],"python")
# print(Sample_tuple.index("Sam"))

# If having existing value then it will get print
# If value is not having in the tuple then will through an error

from operator import is_


fruits = "sapota", "pine", "guava"
is_pine = "pine" in fruits
print(is_pine)

Sample =(1,2,3,False)
print(all(Sample)) # returns false if having element zero/False if not having returns True
    
Sample =(1,2,3,0) # Having zero in the tuple so it will return False
print(all(Sample))

Sample_1 =()
print(all(Sample_1))  # returns True if the tuple is empty