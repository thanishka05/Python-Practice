# # ***Write a program that checks if a number is positive, negative, or zero using an if-elif-else statement***
a = int(input("enter a number :"))
if a > 0:
    print("Positive Number")
elif a<0:
    print("Negtive Number")
else :
    print("It is Zero")

# #*** Write a program to check whether a number is even or odd.***
a = int(input("enter a number :"))
if a %2 ==0:
    print(f"The number {a} is Even")
else :
    print(f"The number {a} is Odd")

# # ***A student passes if they score more than 40 marks. Check if a student has passed or failed.***
score = int(input("Enter the Score "))
if score > 40:
    print("You passed dude (;")
else :
    print("It's gone maynn ):")

# # ***Write a program that takes age as input and categorizes it as:***
# # Child (0-12)
# # Teenager (13-19)
# # Adult (20+)
age = int(input("Enter the age :"))
if age >= 0 and age <= 12:
    print("Your a baby")
elif age >= 13 and age <=19:
     print("Oh! Hi Teen")
elif age >= 20:
    print("Welcome to Adulthood")

# # ***Take a temperature value as input:***
# # Above 30°C: Print "Hot"
# # Between 20°C and 30°C: Print "Warm"
# # Below 20°C: Print "Cold"
temp = int(input("Enter the Temperature: "))
if temp >= 30:
    print("Its Hot , just like you ;)")
elif temp >= 20 and temp < 30:
    print("Thats warm, need a cuddle :)")
elif temp < 20:
    print("Thats too cold, Like your Heart")
import random
# Lucky Draw Winner
# Write a Python program that selects one random winner from the following names:
# ["Akhil", "Meena", "Vikram", "Sai", "Rohit", "Harsha", "Kavya"]
a=["Akhil", "Meena", "Vikram", "Sai", "Rohit", "Harsha", "Kavya"]
b=random.choice(a)
print(f"Hurry {b} your the winner")

# Simulating a Dice Roll 🎲
# Write a program that simulates rolling a 6-sided die and prints the result.
b=random.randint(1,6)
print(f"You dice now shows {b}")


# . OTP Generator 🔢
# Write a program to generate a random 6-digit OTP (One-Time Password)
otp=random.randint(100000,999999)
print(f"Your OTP is {otp} ")

# Coin Toss 🪙
# Write a program to simulate a coin toss and print "Heads" or "Tails" randomly.
coin=["heads","tails"]
side= random.choice(coin)
print("The coin now shows " + side)

# Random Lottery Ticket 🎟️
# Write a program to generate a random lottery ticket with 5 numbers between 1 and 50.
a=[random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)]
print(random.sample(a,5))

# Random Temperature 🌡️
# Write a program that generates a random temperature between -10°C and 45°C and categorizes it as:
# "Cold" (≤ 10°C)
# "Warm" (11°C - 30°C)
# "Hot" (> 30°C)
temp = random.randint(-10,45)
if temp <= 10:
    print(f"Temperature is {temp} so Its cold")
elif temp >= 11 and temp <= 30:
    print(f"Temperature is {temp} so Its warm")
elif temp > 30:
    print(f"Temperature is {temp} so Its hot ")

# . Guess the Number Game 🎯
# Write a number guessing game where the computer selects a random number between 1 and 50 and the user has to guess it.
# The program should keep asking until the user guesses correctly.
guess = random.randint(1,50)
a = int(input("Enter your guess value :"))
if guess == a:
    print("Are you a super computer or what that's Really great mann ,coz I am thinking about {guess} and your answer is also {a} thats a match ")
else:
    print(f"I generated {guess} but your answer is {a} wtf maynn try again")

# Rock, Paper, Scissors ✊📄✂️
# Write a program to play Rock, Paper, Scissors against the computer.
# The computer randomly selects "rock", "paper", or "scissors", and the user inputs their choice.
# The program then determines who wins.
game = ["rock", "paper", "scissors"]
choice = random.choice(game)
us = input("Enter your chocie : ")
if (us == "rock" and  choice == "scissors" or us == "scissors" and choice == "paper" or us == "paper" and choice == "rock"):
    print(f"User is the winner because user choice is {us} and computer choice is {choice}")
elif us == choice :
    print(f"Thats the draw because user choice is {us} and computer choice is {choice}")
else:
    print(f"Computer is the winner because user choice is {us} and computer choice is {choice}")
    