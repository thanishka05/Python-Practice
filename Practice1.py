# Level 1: Basics
# 1. Conditional Statements & Operators
# Write a program that takes a number as input and:
# Prints "Positive" if it is greater than 0
# Prints "Negative" if it is less than 0
# Prints "Zero" if it is 0

a=int(input("enter the number :"))
if a>0:
    print(f"The number {a} is Positive")
elif a<0:
    print(f"The number {a} is Negative")
else:
    print(f"The number {a} is Zero")


# Check if a given number is divisible by both 3 and 5.

a=int(input("enter the number :"))
if a%3 == 0 and a%5 == 0:
    print(f"The number is divisible by 3 and 5") 
elif a%5 == 0:
    print(f"The number is divisible by 5") 
elif a%3 == 0 :
    print(f"The number is divisible by 3 ") 
else :
    print(f"The number is not divisible by 3 or 5") 
    
    
# 2. Random Module
import random
# Generate a random number between 1 and 100. Ask the user to guess the number. Give hints:
# “Too high” if guess > number
# “Too low” if guess < number
# “Correct!” if guess  number
# 
a=random.randint(1,100)
b=int(input("Enter Your Guess :"))
if b>a:
    print(f"Too high{a}")
elif b<a:
    print(f"{a}Too low")
elif b==a:
    print("Correct Guess")
    
# 3. Lists and For Loops
# Given a list of numbers, print only the even numbers using a for loop.
ol=[]
for i in range(6):
    i=int(input("Enter a number "))
    if i%2==0:
        ol.append(i)
print(f"The list if even no's is {ol}")

# Count how many elements in a list are greater than 50.

gr=[]
for i in range(10):
    i=int(input("Enter a number :"))
    if i > 50:
        gr.append(i)
        b=len(gr)
print(f"{b} are greater than 50 in {gr} List")

# Level 2: Combining Topics
# 4. Mini Quiz Generator (random + conditionals)
# Create a list of 5 simple math questions (like 2+3, 5-2, etc.).
# Randomly select one and ask the user.
# Check if their answer is correct.

ques=[("2+5",7),("5-2",3),("8*5",40),("99+100",199),("22+99",121),("5//2",2),("10<<2",40),("22>>2",5)]
que,ans=random.choice(ques)
a=print(f"The Question is : {que}")
c=int(input("Enter You Answer :"))
if c == ans:
    print("Your answer is correct ")
else:
    print("Your answer is incorrect")

# 5. Find the Maximum Odd Number
# Given a list of numbers, write a program to find the largest odd number using for loop and conditionals.
odd =[]
for i in range(10):
    i=int(input("Enter the Number:"))
    if i %2 != 0:
        odd.append(i)
print(f"{odd}, the maxium number in the list is {max(odd)}")