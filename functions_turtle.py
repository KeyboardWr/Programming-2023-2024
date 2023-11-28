# Herman Li
# Nov 18, 2023
# Turtle functions practice

import turtle


BOB = turtle.Turtle()
BOB.color("lightgreen")
BOB.shape("turtle")


def square(numb: float) -> float:

    """Returns the given number squared"""
    return numb ** 2
def draw_square(side_length: float) -> None:
    for _ in range(4):
        BOB.forward(side_length)
        BOB.left(90)
draw_square(25)
draw_square(square(25))


BOB.speed(0)
# Create a squares that get bigger and bigger
for i in range(20):
    draw_square(square(i))
turtle.done()
