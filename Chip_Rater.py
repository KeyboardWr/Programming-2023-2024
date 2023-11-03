# Chip Rater
# Author: Herman Li
# Date: Nov 2, 2023

# Interview people about their perception of the deliciousness 
# We will ask them a set of questions
# In the end, we'll give an aggregate score

# Greet the user
print("Hi, Please answer the questions on the chip you just ate")
# Create a list of questions to ask
questions = [
    "how crispy is the chip on a scale from 1 to 5? 5 is very crispy, 1 is mushy"
    "How would you rate the taste from 1 to 5? 5 is the best chip ever. 1 is garbage"
    "From 1 to 5, how would you rate the packaging? 5 is the best, 1 is terrible"
]

Total_Rating = 0

# For every question in that list
for question in questions:
    print(question)

    # Ask the question

    # Get the user's rating
    user_rating = input().strip(",.?! ").lower()

    # Add the rating to some total-rating
    Total_Rating += user_rating
# Do some math on the results
# Use the average score to represent the chip's rating
average_rating = Total_Rating / len(questions)


# Present the results
print(f"The average rating for this chip is: {average_rating:.2f / 5}")