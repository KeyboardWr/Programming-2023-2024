# Herman Li
# Semester Evaluator Bot
# Nov 3, 2023


import time
# Greet the user and ask how many courses they are staking
print("Hi! I'm going to give you an average score of how much you enjoy your classes.")
time.sleep(.5)
print("1 is the worst and 5 is the best.")
time.sleep(.1)
print(".5 decimals can be used as well")
time.sleep(.2)
classes_taking = input("First, how many classes are you taking this semester?")
time.sleep(.25)
print("Cool, what are your four courses?")
course_1 = input()
course_2 = input()
course_3 = input()
course_4 = input()


course_score = 0
# Loop the question 4 times and ask the user to rate them out of 5
time.sleep(.5)
questions = [f"Ok, how would you rate {course_1} out of 5?", f"how would you rate {course_2} out of 5?"
             ,f"how would you rate {course_3} out of 5?", f"How would you rate {course_4} out of 5?"]

for question in questions:
    User_rating = float(input(question))

    course_score += User_rating
   
    
# Calculate the average score an present a response based on the average
time.sleep(.25)
course_average = course_score / 4
if course_average <1:
    print(f"Ouch, your course average rating is {course_average}")
elif course_average >1:
    print(f"Not a bad semetser, your course average rating is {course_average}")
elif course_average >3:
    print(f"Glad to hear that! Your course average rating is {course_average}")
else:
    print("I don't think you rated your courses properly.")

