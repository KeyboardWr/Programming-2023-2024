# Herman Li
# Similar Hobby Bot
# Nov 14m, 2023

hobby_amount = 0
P1_Hobbies = []
P2_Hobbies = []
similarity_score = 0
import time
print("Hi! I am going to calculate similar hobbies for both of you")
time.sleep(.5)

P1_hobby_amount = int(input("How many hobbies are you going to list for person 1?"))
print("For person 1, please list your hobbies")
for i in range(P1_hobby_amount):
    hobby_amount += 1
    print(f"hobby {hobby_amount}")
    P1_Hobbies.append((input()).lower().strip(",.?! "))

hobby_amount = 0
time.sleep(.25)
print("Great!, what about person 2?")
time.sleep(.2)
P2_hobby_amount = int(input("How many courses is person 2 listing? "))
print("Please list out person 2's hobbies")
for i in range(P2_hobby_amount):
    hobby_amount += 1
    print(f"hobby {hobby_amount}")
    P2_Hobbies.append((input()).lower().strip(",.?! "))

print("It is finally time to calculate hobbies that are similar between you two")
time.sleep(.3)
for hobbies in P1_Hobbies:
    if hobbies in P2_Hobbies:
        similarity_score += 1

print(f"You have {similarity_score} hobbies in common between you and the other person")



