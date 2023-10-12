# Herman
# Loop Practice Bot
# Oct 10, 2023
import time
# Create a list of grocceries
grocceries = ["hot wheels","lego", "video games", "Ice cream"]

# Do something for each thing in the list
# Pinrt it out in a pretty way (Like an actual list)

for item in grocceries:
    print(f"* {item}*")
    print("  ----")

#Create a pyramid like this using a for loop

# .
# ..
# ...
# ....
# .....

pyramid = ["*","**","***","****","*****"]
for item in pyramid:
    print(item)

# Create a new years eve countwodn
# Start at 10 
# Countdown every second
# After 10 seconds print happy new year

new_year = ["10", "9", "8","7","6","5","4","3","2","1","Happy New Year!"]

for item in new_year:
    print(item)
    time.sleep(1)

