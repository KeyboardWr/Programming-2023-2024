# Author: Herman Li
# Mcdonalds Bot
# Date: Nov 3, 2023

# Ask if the customer wants a burger and add it to the total cost depending on the response
total_cost = 0

decision_for_burger = input("Hello potential customer! Would you like a burger for $5? Yes/No").lower().strip(",.?! ")
if decision_for_burger == "yes":
    total_cost += 5
elif decision_for_burger == "no":
    print("Ok, your lose")
else:
    print("sorry I don't know what that means")
# Now ask for fries
decision_for_fries = input("How about some fries for $3? Yes/No").lower().strip(",.?! ")
if decision_for_fries == "yes":
    total_cost += 3
elif decision_for_fries == "no":
    print("You're apparently not that hungry I guess.")
else:
    print("Sorry I don't know what that means")

# Calculate the total with 14% tax
print(f"Nice, your total including tax is {total_cost + total_cost * 0.14}")
    
