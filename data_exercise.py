from pathlib import Path


# File Exercises
# Author: Herman Li
# Nov 16, 2023

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        whole_thing = line.split(",")
        print(whole_thing)
    

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        whole_thing = line.split(",")
        print(whole_thing)
    

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
Chicken_A_Likes = ["Chicken Adobo"]

with open("./data_example.csv", encoding="utf-8") as f:
    chicken_sim_score = 0
    for line in f:
        for item in Chicken_A_Likes:
            whole_thing = line.split(",")
            if item in whole_thing:
                chicken_sim_score +=1
    print(f"{chicken_sim_score} people like Chicken Adobo")


# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".
People_starting_with_A = 0
Letter_in_Name = ("A")
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        whole_thing = line.split(",")
        names = whole_thing[0]
        for name in names:
            if name[0] == Letter_in_Name:
                People_starting_with_A += 1
    print(f"{People_starting_with_A} have A as their first letter of their name")

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?
People_in_Guangzhou = 0
china_city = ["Guangzhou\n"]
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        whole_thing = line.split(",")
        for item in china_city:
            if item in whole_thing:
                People_in_Guangzhou += 1 
    print(f"{People_in_Guangzhou} person is from Guangzhou")

# Problem 6:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.


# Problem 7:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?
foods = []
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        whole_thing = line.split("\n")
        whole_thing = line.split(",")
        possible_foods = whole_thing[1]
        foods.append(possible_foods)

    from collections import Counter
    def most_frequent(foods):
        occurence_count = Counter(foods)
        return occurence_count.most_common(1)[0][0]
    print(f"Apparently the {most_frequent(foods)} is the most liked dish for this data")
