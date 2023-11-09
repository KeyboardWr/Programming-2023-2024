# Herman Li
# Semester Evaluator Bot
# Nov 3, 2023

import time
# Greet the user and ask how many courses they are staking
print("Hi! I'm going to give you an average score of how much you enjoy your classes.")
time.sleep(1)
print("1 being the worst and 5 being the best.")
time.sleep(1)
print(".5 decimals can be used as well")
time.sleep(1)
classes_taking = int(input("First, how many classes are you taking this semester?"))
time.sleep(.5)
print(f"Great, what are your {classes_taking} courses?") 
time.sleep(.2)
course_number = 0 
courses = []
for i in range(classes_taking):
    course_number += 1
    courses.append(input(f"course {course_number}:").lower().strip(",.?! "))
   
course_score = 0
# Loop the question x amount of times and ask the user to rate them out of 5
time.sleep(.5)
print("Nice!")
time.sleep(.2)
for item in courses:
    user_rating = float(input(f"How would you rate {item} course out of 5? "))

    course_score += user_rating
   
# Calculate the average score an present a response based on the average
time.sleep(.25)
course_average = course_score / classes_taking

if course_average <1:
    print(f"Ouch, your course average rating is {course_average}")
elif course_average >1 and course_average <3:
    print(f"Not a bad semetser, your course average rating is {course_average}")
elif course_average >3:
    print(f"Glad to hear that! Your course average rating is {course_average}")
else:
    print("I don't think you rated your courses properly out of 5.")

