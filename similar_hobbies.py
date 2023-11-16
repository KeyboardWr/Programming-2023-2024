# Herman Li
# Similar Hobby Bot
# Nov 14m, 2023

hobby_amount = 0

similarity_score = 0
import time
print("Hi! I am going to calculate similar hobbies for both of you")
time.sleep(.5)

P1_hobby_amount = int(input("How many hobbies are you going to list for person 1?"))
time.sleep(.3)
print(f"For person 1, please list your {P1_hobby_amount} hobbies separated by spaces, then press enter when you typed out your answers")
P1_Hobbies = input().split(" ")

hobby_amount = 0
time.sleep(.25)
print("Great!, what about person 2?")
time.sleep(.2)
P2_hobby_amount = int(input("How many courses is person 2 listing? "))
print(f"Please list out the {P2_hobby_amount} hobbies separated by spaces, then press enter when you typed out your answers")
P2_Hobbies = input().split(" ")
time.sleep(.2)
print("It is finally time to calculate hobbies that are similar between you two")
time.sleep(.3)
for hobbies in P1_Hobbies:
    if hobbies in P2_Hobbies:
        similarity_score += 1

print(f"You have {similarity_score} hobbies in common between you and the other person")



