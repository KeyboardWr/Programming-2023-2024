# Author: Herman Li
# Function Practice
# Nov 24, 2023


def area_of_a_square(sidelength: float):
	"""Calculates the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square"""

	area = sidelength ** 2
	
	print(f"The area of a square with side length = {sidelength} is: {area} square units")

area_of_a_square(12.2)  # 12.2 is the argument