# Herman Li
# Parental Bot
# Nov 16, 2023

import time
print("Hi! I am parent bot")
time.sleep(.5)
print("I am going to ask 4 questions and using my parental skills, do something depending on your response")

user_status_response= 0

questions = ["Did you eat?", "Did you study?", "Did you do your laundry?", "Did you call grandma?"]

for question in questions:
    user_response = (input(question).lower().strip(",.?! "))
    if user_response == "yes":
        user_status_response += 1


if user_status_response == 0:
    print("I'm coming over")
elif user_status_response == 1 or  user_status_response == 2:
    print("Ok")
elif user_status_response == 3 or user_status_response == 4:
    print("Good!")
else:
    print("I don't think you responded correctly to my questions")
