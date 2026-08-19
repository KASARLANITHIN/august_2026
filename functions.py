#syntax
# def fn():
    #code to be executed
    #function body


# num_1 = int(input("enter the number: "))
# print(num_1)

# def greet():#function definition
#     num_1 = int(input("enter the number: ")) #function body
#     print(num_1) #function body
#     print("welcome to pythonlife")
# greet() #function calling
# greet()
# greet()
# greet()
# greet()


# def add():#function definition
#     num_1 = int(input("enter the number: "))
#     num_2 = int(input("enter the number: "))
#     print(num_1+num_2)
# add()#function calling


#parameters and arguments
# def add(num_1,num_2):#function definition
#     print(num_1+num_2)



# num_1 = int(input("enter the number: "))
# num_2 = int(input("enter the number2: "))
# add(num_1,num_2)#function calling,here 10,10 are the arguments passed to the function parameters





# def add(a,b):#function definition
#     return a+b
# obj = add(10,10)
# print(obj*25)


# arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)

# def sample(*a):
#     print(a)
# sample(1,2,3,True,"welcome to pythonlife",[1,2,3])


#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
#**

# def sample(**a):
#     print(a)
# sample(a=1,b=2,c=3)
# sample(a="nithin",b= "raki",c="sahail")

# * --> tuple #all
# ** --> dictionary 


# def details(user=None,empid=None,dept=None):
#     print(user,empid,dept)
# details("nuthan",7891,"python")
# details("raki",46549,)
# details("sahail",)
# details()



# def discount(price,discount=20):
#     discount = (price*discount)/100
#     final_price = price-discount
#     return final_price
# print(discount(10000))
# print(discount(50000))
# print(discount(60000))
# print(discount(100000,50))



#variables --> local variables  (inside the function ) 2. global var --> outside the function
# def details():
#     user = "nithin"
#     empid = 4860
#     salary = 260000
#     print(user)
#     print(empid)
#     print(salary)
#     hike = 100000
#     salary+=hike
#     print(f"salary after hike {salary}")

# details()



# balance = 1000
# def credit(amount):
#     global balance
#     print(amount)
#     balance+=amount
#     print(balance)
# credit(5000)


# print(balance)



# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)


# add(10,10)
# expo(10,4)
# expo(1,42)
# expo(12,4)
# expo(17,4)





# balance = 1000
# mini = []
# def credit(amount):
#     pass

# def debit():
#     global balance
#     if balance >amount:
#         balance -= amount
#     else:



# def balance():
#     pass

# def ministatement():
#     pass

# while True:
#     print("1. credit")
#     print("1. credit")
#     print("1. credit")
#     print("1. credit")
#     choice = input("enter your choice: ")
#     if choice == "1":
#         amount = int(input("enter the amount"))
#         credit(amount)



# list_1 = ["allu arjun"]
# print(list_1.count("allu arjun"))