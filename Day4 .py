# ////List Sum & Average////
# Take 5 numbers as input and store them in a list.
# Print the sum and average of the numbers.
import random
a=[]
b=0
for i in range(5):
    num = int(input("Enter a Number : "))
    a.append(num)
for num in a:
    b+=num
c=b/len(a)
# print(f"the average the numbers in list is {c} and the sum of the numbers in list is {b}")
# ////Find the Largest Number////
# Take 5 numbers as input and find the largest one using max().
import random
a=[]
for i in range(5):
    num=random.randint(0,100)
    a.append(num)
print(a)
d=max(a)
print(f"The largest number in the list is {d}")
#//// Number Sorting////
# Take 5 numbers, store them in a list, and print them sorted in ascending order.
a=[]
for i in range(5):
    num=int(input(f"Enter the {i+1} number :"))
    a.append(num)
c=sorted(a,reverse=False)
print(c)
# ////Shuffled List////
# Store 5 names in a list.
# Shuffle the list and print the new order.
import random
a=["Thani","pani","kani","vani","veni"]
random.shuffle(a)
print(a)
#//// Multiplication Table////
# Take a number as input.
# Print its multiplication table up to 10 using a for loop.
a=int(input("Enter a number :"))
for i in range(11):
    print(f"the table for number you given is {a*i}")