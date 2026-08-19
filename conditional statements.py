# # # # #syntax
#if condition:
#   statement 1
#   statement 2
#   statement 3

# age = 23
# if age>=23:
#     print(f"you are eligible to vote age is {age}")
#     user_name = input("enter the user_name: ")
#     print(user_name)

# #Else 
#if condition :
     #code block to execute if condition is true
#else:
    #code block to execute if condition is false


# age = int(input("enter tha age: "))
# if age>=65:
#     print(f"you are eligible to vote age is {age}")
# else:
#     print(f"you are not eligible to vote age is {age} under 18")

# user_name = input("enter the user_name: ")
# password = input("enter the password: ")
# if user_name == "nithin" and "nithin@123":
#     print(f"login success")
#     print(f"welcome arjun")
# else :
#     print(f"invalid credentials")

#if-elif-else:
#if condition_1:
#    statement 1
#elif condition_2:
#   statement 2
    #elif condition_3:
#   statement 3
    #else :
#   statement

#grading system
# marks = int(input("enter the marks: "))
# if marks>=90:
# # #    print(f"a grade {marks}")
# # # elif marks>=80:
# # #     print(f"b grade {marks}")
# # # elif marks>=70:
# # #     print(f"c grade {marks}")
# # # elif marks<=34:
# # #     print(f"failed..")

# # #2 Age Group Classification Program
# # #input as user age
# # # Age Group Classification
# # age = int(input("Enter your age: "))
# # if age >= 0 and age <= 12:
# #     print("Child")
# # elif age >= 12 and age <=17:
# #     print("Teenager")
# # elif age >= 18 and age <= 64:
# #     print("Adult")
# # elif age >= 65:
# #     print("Senior")
# else:
 #     print("Invalid age")

# Vowel Checker:
# Write a Python program that takes a character as input and checks whether 
# it is a vowel or not. Use the if-else statement.

# char = input("enter the character: ") 
# vowels = "aeiouAEIOU"
# if char in vowels:
#     print("vowel")
# else:
#     print("not vowel")

#3. Number Classifier:
# Write a program that takes an integer as input and classifies it as positive, 
# negative, or zero. Use the if-elif-else statement.

# num_1 = int(input("enter the number: "))
# if num_1 > 0:
#     print(f"{num_1} is a postive num")
# elif num_1 < 0:
#     print(f"{num_1} is negative num")
# else:
#     print(f" {num_1} is zero")

# îµî‚” Leap Year Checker:
# Create a program that checks whether a given year is a leap year or not. A 
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.
# year = int(input("enter the year: "))
# if (year %400 ==0) or (year % 4 == 0 and year % 100 != 0):
#     print(f" leap year")
# else:
#     print(f" not a leap year")

# î¶î‚”Calculator:
# Build a simple calculator program that takes two numbers and an operator 
# (+, -, *, /) as input and performs the corresponding operation.

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))
# if operator == "+":
#     print("addition operator result=", num1=num2)
# elif operator== "/":
#     print("division operartor result=", num/num2)
# elif operator == "*":
#     print("multiplication operator result+", num1*num2)
# elif operator == "-":
#     print("multiplication operator result:", num1- num2)
# else:
#     print("operator is invalid")


# 6. Short Hand If: Rewrite the following code using the short-hand if statement:
# x = 8
# if x % 2 == 0: result = "Even"
# # else: result = "Odd"
# x = int(input("enter the num: "))
# print(f"{x} is a even num") if x%2==0 else (f"{x} is a odd num")
# #or
# result = "even" if ("x%2=0") else "odd"

# î‚”Discount Calculator:
# Create a program that calculates the final price after applying a discount. 
# The program should take the original price and the discount percentage as 
# # input.
# price = float(input("Enter the original price: "))
# discount = float(input("enter the discount price: "))

# discount = (price * discount)/100 
# final_price = price - discount
# print ("discount:", discount)
# # print("final-price:", final_price)

#  BMI Calculator:
# Write a program that calculates the Body Mass Index î‚BMIî‚‚ using the 
# formula: BMI î‚› weight (kg) / (height (m))^2. The program should take 
# weight and height as input.
#below code is the calculation for BMI, 3rd line refers to BMI = weight/height*height
# weight = float(input("Enter your weight (kg): "))
# height = float(input("Enter your height (m): "))
# height_square = height * height
# bmi = weight / height_square
# print("BMI =", bmi)