# //////Name Formatter/////
# Take first name and last name as input.
# Print them in the format: "Hello, Firstname Lastname! Your name has X characters."
# Use f-strings and len() to count characters (excluding spaces).
a= input("Enter your First Name :")
b= input("Enter your Last Name :")
c=len(a)
d=len(b)
e=c+d
print(f"Hello {a} {b}! Your name has {e} characters.")
# /////Age in 5 Years/////
# Ask the user for their name and age.
# Print: "Hey [name], you will be [age+5] years old in 5 years!"
a= input("Enter your Name :")
b= input("Enter your Age :")
print(f"Hey {a}, you will be {b+5} years old in 5 years!")
# ////Word Repeater////
# Take a word and a number as input.
# Print the word repeated that many times (use type casting)
a = input("Enter the Word :")
b = int(input("Enter the number of times to repeat: "))
print(f"The word '{a}' repeated {b} times: {a * b}")
