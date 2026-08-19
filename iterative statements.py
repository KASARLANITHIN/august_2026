# LOOPS & ITERATIVE STATEMENTS...

# TASK-1 Sum of Squares
'''Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a 
for loop.'''

sum = 0
for i in range(1,6):
    result = i**2
    print(result)  # printing squares of input
    sum+= result  # sum of the squares
print(sum)

# TASK-2 Exercise 2î‚’ Countdown
'''Write a Python program that uses a 
while loop to print a countdown from 5 to 1.'''

count = 5
while  count>=1:
    print(count)
    count-= 1

# TASK-3  Multiplication Table with Nested For Loop
'''Write a Python program to print the multiplication table for a user-specified 
number using a nested for loop.'''    

num = int(input("enter a input:"))
for i in range(0,11):
    for j in range(1):
        print(f"{num} X {i} = {num*i}")

# TASK-4  
'''Calculate the sum of all numbers from 1 to a given number'''
num = int(input("enter a value:"))
sum = 0
for i in range (0,10+num):
    sum+= i 
    print(sum)


# TASK-5   
'''Write a Python program that uses a "for" loop to find the sum of all even 
numbers between 0 and 10 (inclusive).'''  
sum = 0
for i in range (11):
    if i%2==0:
        sum+= i
        print(sum)
print(i) 


# TASK-6 
'''Display numbers from -10 to -1 using for loop'''
for i in range(-10,0):
    print(i)
print(f"The last iteration {i}")


# TASK-7 
'''Write a Python program to print the cube of all numbers from 1 to a given 
number'''
n = int(input("enter value :"))
for i in range (1,n+1):
    result = i**3
    print(result)

print(i)