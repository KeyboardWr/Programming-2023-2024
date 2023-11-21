# Herman Li
# Turtle Bot
# Nov 21, 2023


import turtle

# ----- Constants
TURTLE_MAGNITUDE = 20
# Create a turtle
michaelangelo = turtle.Turtle()


# Get some instructions from the user
print("""To give commands, type:
F - to go forward
L - to go left
R - to go right
B - to go backwards
Stop - to stop""")

command = input("Where should I go?")

# Repeat the below code INDEFINITELY
done = False

while not done:
    command = input("Where should I go?")
    # Based on those intructions, move the turtle on the screen
    if command.strip(",.?! ").lower() == "F":
        michaelangelo.forward(TURTLE_MAGNITUDE)

    # YOU DO NOW --- implement left and right
    elif command.strip(",.?! ").lower() in ["L, Left"]:
        michaelangelo.left(90)

    elif command.strip(",.?! ").lower() in ["R, Right"]:
        michaelangelo.right(90)
    elif command in ["b" "backwards"]:
        michaelangelo.backward(TURTLE_MAGNITUDE)

    elif command.strip(",.?! ").lower() == "Stop":
        done = True


turtle.done()
