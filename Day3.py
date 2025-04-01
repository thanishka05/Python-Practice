# ////Random Choice////
# Store 5 colors in a list.
# Print a random color from the list using random.choice().
import random 
colors = ["green","pink","yellow","white","black"]
fav = random.choice(colors)
print(fav)
# ////Sentence Word Counter////
# Take a sentence as input and split it into words.
# Print the number of words in the sentence.
a=input("Enter a sentence : ").split(" ")
b=len(a)
print(f"the sentence as {b} words")
#//// Math Quiz ////
# Generate two random numbers (1-10).
# Ask the user to add them.
# Check if the answer is correct.
import random
ran_num = random.randrange(1,11)
ran_num2 = random.randrange(1,11)
user_answer = int(input(f"What is {ran_num} + {ran_num2}? "))
correct_answer = ran_num + ran_num2
if user_answer == correct_answer:
    print("Correct! Well done. 🎉")
else:
    print(f"Wrong! The correct answer is {correct_answer}.")