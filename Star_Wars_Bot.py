# Herman
# Star Wars Bot
# October 16, 2023

import time

print("Hellos User!")
time.sleep(.5)
print("I will simply tell you if you belong to the dark side or light side")
time.sleep(1)
print("With only a single question")

dark_side_factor = input("Do you like capes and the colour red?")

if dark_side_factor.lower().strip(",?. !") == "yes":
    print("judging by your response...")
    time.sleep(1)
    print("You are worthy of being on the dark side! Rule the galaxy!")

elif dark_side_factor.lower().strip(",.?! ") == "no":
    print("Only the dark side is available for chosen ones")
    time.sleep(.5)
    print("You belong to the light side")

else:
    print("Sorry I couldn't interpret what you mean")


