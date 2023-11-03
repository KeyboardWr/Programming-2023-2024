# Bubble Tea Popularity Algorithm
# Herman Li
#October 27, 2023
coco_likes = 0
Chatime_likes = 0
Bubble_Q = 0
Sun_tea_Like = 0
Xing_fu_Likes = 0
NUMB_RESPONDENTS = 5
# Ask 5 users what their favourite bubble tea place is
# Print out summary of the data

import time
for _ in range(NUMB_RESPONDENTS):


    # Ask the user what their favourite tea place is

    # Tallying/Counting Algo
    # Options: Coco, Chatime, Sun Tea, Xing Fu Tang, Bubble Queen
    # If they say Coco, increase the counter for Coco by one

    # Print out the results
    print("What's your favourite bubble tea place?")
    fave_bbt = input().strip(", . ? !").lower()

    if fave_bbt == "coco":
        coco_likes = coco_likes + 1 
    elif fave_bbt == "chatime":
        Chatime_likes += 1
    elif fave_bbt == "suntea":
        Sun_tea_Like =+ 1
    elif fave_bbt == "Bubble Queen":
        Bubble_Q += 1
    elif fave_bbt == "xing fu":
        Xing_fu_Likes += 1
    else:
        print("sorry I don't know what that means")



 # Print a summary of the results
print("The final results are")
time.sleep(1)
print(f"cocolikes: {coco_likes / NUMB_RESPONDENTS * 100}%")
time.sleep(.5)
print(f"Bubble Queen Likes: {Bubble_Q / NUMB_RESPONDENTS * 100}%")
time.sleep(.5)
print(f"xing fu likes: {Xing_fu_Likes / NUMB_RESPONDENTS * 100}%")
time.sleep(.5)
print(f"Chatime Likes: {Chatime_likes / NUMB_RESPONDENTS * 100}%")
time.sleep(.5)
print(f"SunTea likes: {Sun_tea_Like / NUMB_RESPONDENTS * 100}%")