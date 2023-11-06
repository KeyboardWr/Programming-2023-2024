# Author: Herman Li
# Olympic Judging Bot
# Nov 3, 2023

import random 
import time
# Dive into the water to recieve a score from 5 judges
print("You will have 5 times to dive")
time.sleep(.5)
input("TRIAL 1: Type 'dive' to jump in the water and impress the judges").lower().strip(",.?! ")
time.sleep(.5)


# Create the judges and randomly rank the dive out of 10
judge_score = [1, 1.5, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]

Judge_1 = random.choice(judge_score)
Judge_2 = random.choice(judge_score)
Judge_3 = random.choice(judge_score)
Judge_4 = random.choice(judge_score)
Judge_5 = random.choice(judge_score)

print(f"Judge 1 ranks you {Judge_1}")
time.sleep(.5)
input("TRIAL 2: Type 'dive' again to jump in the water and impress the judge 2").lower().strip(",.?! ")
time.sleep(.2)
print(f"Judge 2 scores you {Judge_2}")
input("TRIAL 3: Type 'dive' again to jump in the water and impress the judge 3").lower().strip(",.?! ")
time.sleep(.2)
print(f"Judge 3 scores you {Judge_3}")
time.sleep(.2)
input("TRIAL 4: Type 'dive' again to jump in the water and impress the judge 4").lower().strip(",.?! ")
time.sleep(.2)
print(f"Judge 4 scores you {Judge_4}")
time.sleep(.2)
input("TRIAL 5: Type 'dive' again to jump in the water and impress the judge 5").lower().strip(",.?! ")
print(f"Judge 5 scores you {Judge_5}")
time.sleep(.2)

# Present all the scores
print(f"Judge 1: {Judge_1}")
print(f"Judge 2: {Judge_2}")
print(f"Judge 3: {Judge_3}")
print(f"Judge 4: {Judge_4}")
print(f"Judge 5: {Judge_5}")
time.sleep(.2)

# Calculate the average score 
print(f"Your average score for your dive is {(Judge_1 + Judge_2 + Judge_3 + Judge_4 + Judge_5) / 5}")