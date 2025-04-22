import random
# Random Password Generator
# Write a function generate_password(length) that returns a random password 
# with the given length using lowercase letters and numbers. Use random.choice().

# def generate_password(lengthy):
#     character="qwertyuiopasdfghjklzxcvbnm1234567890"
#     password =""
#     for i in range(lengthy):
#         password+=random.choice(character)
#     return password
# kl=int(input("Enter the Length of password you need:"))
# print(generate_password(kl))

# Count Vowels
# Write a function count_vowels(s) that returns the number of vowels in a string.

# def count_vowels(s):
#     tot=s.count("a")+s.count("e")+s.count("i")+s.count("u")+s.count("o")
#     print(f"The vowels in the sentence you entered are {tot}")
#     return tot
# s=input("Enter any Sentence you want :").lower()
# count_vowels(s)

# List Filter - Only Even Numbers
# Write a function filter_even(lst) that returns a new list with only even numbers from the given list
# def filter_even(lst):
def filter_even(lst) :
    new_list=[]  
    if num % 2==0:
        new_list+=num
    return new_list
lst=[]
for i in range(10):
    num=int(input("Enter the number :"))
    lst.append(num)
filter_even(lst)
def filter_even(lst):
    new_list = []
    for num in lst:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

# Getting input list from user
lst = []
for i in range(10):
    num = int(input("Enter the number: "))
    lst.append(num)

even_numbers = filter_even(lst)
print("Even numbers from the list:", even_numbers)
