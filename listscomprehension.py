# 1. Squares of Numbers
# Create a list of squares from 1 to 10.

# squares = [i**2 for i in range(1,11)]
# print(squares)


# 2. Even Numbers Between 1 to 20
# Create a list of all even numbers from 1 to 20

# even = [x for x in range (1,21) if x % 2 == 0]
# print(even)


# 3. First Letter of Each Word
# From the list ["apple", "banana", "cherry", "date"], create a list of their first letters.

# a=["apple", "banana", "cherry", "date"]
# b=[char[0] for char in a  ]
# print(b)

#  4. Convert to Uppercase
# Convert each word in a list to uppercase.
# Input: ["red", "blue", "green"]

# a= ["red", "blue", "green"]
# b=[i.upper() for i in a ]
# print(b)


# 5.Filter Numbers Divisible by 3
# From numbers 1 to 30, create a list of numbers divisible by 3.

# three=[x for x in range(1,31) if x%3==0]
# print(three)


# 6.Label Numbers Odd or Even
# From 1 to 10, create a list like ["odd", "even", "odd", ...]

# label=["even" if i % 2==0 else "odd" for i in range(1,11)]
# print(label)


#  8. Remove Vowels from a Word
# Given the word "engineering", create a list of all consonants (remove vowels).

# new_list= [char for char in "engineering" if char not in 'aeiou']
# print(new_list)


# 9. Reverse Words in List

# words = ["car", "bike", "bus"]
# rev=[cha[::-1] for cha in words]
# print(rev)

# 10. Multiply Corresponding Elements of Two Lists

# a = [1, 2, 3]
# b = [4, 5, 6]
# # num=[]
# # for i in range(len(a)):
# #     num.append(a[i]*b[i])
# # print(num)

# new=[a[i]*b[i] for i in range(len(a))]
# print(new)

def greet():
    return("Hello, welcome to Python!")

greet()  # Calling the function
    

    