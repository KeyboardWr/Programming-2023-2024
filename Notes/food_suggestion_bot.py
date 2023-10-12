# Herman
# Oct 6, 2023
# Food Chabot

import random
import time

# A bot that asks the user what their favourite food is
# The bot identifies the type/cuisine of the food 
# and offers a suggestion


# Introduce 
# Ask the user what their favourite food is
print("Hello I am here to suggest a resteraunt to you")
time.sleep (.5)
fave_food = input("Tell me what your favourite food is")




# If user answers with an Italian dish
#List all italian dishes
# Suggest an Italian restaurant
italian_food = ["pizza", "pasta", "lasagna", "tiramisu"]
chinese_food = ["fried rice", "noodle soup" "dumpings", "dim sum", "sticky rice"]

if fave_food.lower().strip(",.?! ") in italian_food:
    print("I think you might like italian food🇮🇹")
    time.sleep(.5)
    print("I recommend The Old Spaghetti Factory")
    time.sleep(.2)
    print("Heres the address: Riverport Entertainment Complex, 14200 Entertainment Blvd #110, Richmond, BC V6W 1K3")
elif fave_food.lower().strip(",.?! ") in chinese_food:
    print("I see you like chinese food🇨🇳")
    time.sleep(.5)
    print("I recommend Hong Kong Flavour")
    time.sleep(.5)
    print("Here's the address: 10151 No. 3 Rd #104, Richmond, BC V7A 4R6")
else:
    print("Sorry I don't recognize your favourite food")