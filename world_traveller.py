# Herman Li
# World Traveller Bot
# Nov 3, 2023
import time
# Ask the user if he has been to each continent
continents_travelled = 0
continents = ["North America", "South America", "Europe", "Asia", "Antartica","Australia", "Africa"]
for item in continents:
    user_response = input(f"Have you been to {item}?").lower().strip(",.?! ")
    if user_response == "yes":
        continents_travelled += 1
    elif user_response == "no":
        print("ok")
    else:
        print("Sorry I don't know what that means")

time.sleep(.5)
print(f"Based on what you said, you have been to {continents_travelled}/7 continents")

