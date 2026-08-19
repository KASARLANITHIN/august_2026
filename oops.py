#syntax
# class classname():
    #attr
    #methods

# def details(self,):#methods
#     print(f"he works at ABC company.{self}")

# details(10)


# class person_details():#class definition
#     user_name = "nithin"#attributes
#     emp_id = 1234
#     def details(self,):#methods
#         print(f"he works at ABC company.{self.user_name}")
#     def details2(self,):
#         print(f"he owns ABC company.")
#         self.details()

#syntax
# objname = classname()
# nithin = person_details()
# nithin.details()
# nithin.details2()
# print(nithin.user_name)
# nithin.details2()



# class feature_phone():
#     brand = "nokia"
#     color = "black"
#     batter = "3000mah"
#     def calling(self,mob_num,brand_name):
#         print(f"you are calling from {brand_name}......{mob_num}")
#     def message(self,message):
#         print(f"{message} sent succesfully....")
# #objname = classname()
# nokia = feature_phone()
# nokia.calling(123456498,"nokia")
# nokia.message("hello everyone")
# samsung = feature_phone()
# samsung.calling(54989,"samsung")
# celkon = feature_phone()
# celkon.calling(15649498,"celkon")





# class feature_phone():
#     def __init__(self,bn,color="black",battery=5000):
#         self.bn = bn
#         self.color = color
#         self.battery = battery
#     def calling(self,):
#         print(f"you are calling from {self.bn}")
#         print(f"brand color {self.color}")
#     def message(self,message):
#         print(f"{message} sent succesfully....")
# nokia = feature_phone("nokia","black",5000)
# nokia.calling()


# samsung = feature_phone("samsung",)
# samsung.calling()





# class feature_phone():
#     def __init__(self,bn,color,battery):
#         self.bn = bn
#         self.color = color
#         self.battery = battery
#     def calling(self,):
#         print(f"you are calling from {self.bn}")
#     def message(self,message):
#         print(f"{message} sent succesfully....")
# class smartphone(feature_phone):
#     def gaming(self):
#         print(f"playing BGMI ")
#     def browsing(self,browser):
#         print(f"browsing internet from {browser}")
# samsung = smartphone("samsung","white",5000)
# samsung.gaming()
# samsung.browsing("chrome")
# samsung.calling()
# samsung.message("hello everyone")



# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")

# obj1 = b()
# obj1.child1()
# obj1.parent()
# obj2 = c()
# obj2.child2()
# obj2.parent()


# # multiple inheritance -->multiple base class one derived class
# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")

# obj = child()
# obj.child()
# obj.mother()
# obj.father()








# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output1(self):
#         print(f"this is father class")
# class child(father):
#     def output2(self):
#         print(f"this is child class")
#     def sample(self):
#         print(f"started ABC company")
# obj = child()
# obj.output2()
# obj.sample()
# obj.output1()
# obj.output()



# class ATM():
#     def __init__(self,bank,location,branch,balance = 1000,pin_number=1234):
#         self.bank = bank
#         self.location = location
#         self.branch = branch
#         self._balance = balance
#         self.__pin_number = pin_number
#     def credit(self,credi_a):
#         pass
#     def debit(self,):
#         pass
# class ATM2(ATM):
#     def balance(self,):
#         pass
#     def ministatemtn(self,):
#         pass

# while True:
#     sbin = ATM2("sbin","katedhan","bible house",10000)
#     print("1.credit")
#     print("2.debit")
#     print("3.balance")
#     print("4.ministatement")
#     print("5.exit")
#     choice = int(input("enter your options"))
#     if choice == 1:
#         credit_amount = int(input("enter the amount to credit: "))
#         sbin.credit(credit_amount)


# num_1 = int(input("enter the number: "))
# print(num_1)


################  august 07 2026  ###########
# polymorphism--> implementing same thing in different forms
# 1.overloading --> 1.operator overloading 2.method overloading
# 2.method overriding'

# (+)
# num_1 = 10
# num_2 = 10
# print(num_1+num_2)


# user = "python"
# user2 = "life"
# print(user+user2)



#method overloading --> method name should be same
#arguments must be different --> in the terms of length or type of arguments
# class calculator():
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = calculator()
# obj.add(10,10)


# class calculator():
#     def add(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10,)
# obj.add(10,)
# obj.add()
# obj.add("nithin","pythonlife","nani")
# obj.add("nithin",)
# obj.add("nithin",1234,"pythonlife")

#2.method overriding
# method overriding --> method name should be same arguments should be also same
# class father():
#     def details(self,a):
#         print(f"this is parent class")
# class child(father):
#     def details(self,a):
#         print(f"this derived class..")
#         super().details("100cr")
# obj = child()
# obj.details("100cr")


# public
# protect _
# private __

# class gfather():
#     def __init__(self,a):
#         self._a = a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is derived class {self._a}")
# obj = father("100cr")
# obj.details()




# class gfather():
#     def __init__(self,a):
#         self.__a = a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is derived class {self.__a}")
# obj = father("100cr")
# obj.details()



# class sbin():
#     def __init__(self,a):


#data abstraction --> hiding the implementation and showing only essential part
# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module

# from abc import ABC,abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self,):
#         pass
#     @abstractmethod
#     def display_2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print(f"implementation 1 done ")

#     def display_2(self):
#         print(f"implementation 2 done")
# obj = demo()
# obj.display()
# obj.display_2()




from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class gpay(payment):
    def pay(self):
        print(f"payment received")
class phonpe(payment):
    def pay(self):
        print(f"payment received")
class cred(payment):
    def pay(self):
        print(f"payment received")
    def cashback(self):
        print(f"casback received")
gpe = gpay()
gpe.pay()

phonepe = phonpe()
phonepe.pay()

cred1 = cred()
cred1.pay()
cred1.cashback()