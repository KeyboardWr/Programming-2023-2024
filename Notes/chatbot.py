#ChatBot
#Author: Herman
#Date: 21 Septmeber 2023

import random 
import time

#Greet the user
#Pause in between lines of dialogue
#Get the user's name and store in a varialbe
#Respond with the user's name

#Ask the user what their favourite food is

#REspond

print("Hi i m chatbot")
time.sleep(2)

user_name = input("what is yur name")

time.sleep (1.5)

#Create a list of appropriate responses 
#Choose one response randomly from the list
#Print the chosen response
list_of_fave_food_responses = [
    "wow thats cool", "thats my name too", "awesome!" "sounds unique"
]


random_response = random.choice(list_of_fave_food_responses)
print(random_response)


print(list_of_fave_food_responses[2])

#Ask what the user's favourite food is
print("What's your favourite food?")

fave_food = input("What's your favourite food?")

#If they answer pasta, respond with pasta response
if fave_food == "pasta":
    print("I also like Italian food")
#If response is suishi, respond with having similar fav foods
elif fave_food == "sushi":
    print("That's my favourite food too")
elif fave_food == "Fried Rice":
    print("That is a good choice")
#If none respond with thats soundss good
else:
    print(random.choice(list_of_fave_food_responses))