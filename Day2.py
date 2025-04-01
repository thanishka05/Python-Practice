#//// Vowel Counter////
# Take a sentence as input and count how many times 'a', 'e', 'i', 'o', 'u' appear.
# Use lower() to handle uppercase letters.
a=input("Enter a Sentence of your choice : ").lower()
b=a.count('a')+a.count('e')+a.count('i')+a.count('o')+a.count('u')
print(f"In the sentence {a} there are {b} vowels")
# ///Even or Odd///
# Take an integer input and print if it's even or odd.
# a = int(input("Enter any number :"))
if a % 2 ==0:
    print(f"The Number {a} is a Even Number")
else:
    print(f"The Number {a} is a Odd Number")
# ////Login System////
# Ask for a username and password.
# If the username is "admin" and the password is "1234", print "Login Successful";
# otherwise, print "Invalid Credentials".
a = input("Enter the username: ")
b = input("Enter the Password :")
if a=="admin" and b=="1234":
    print("Login Successful")
else:
    print("Invalid Credentials")