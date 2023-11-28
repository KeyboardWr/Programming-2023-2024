# Author: Herman Li
# Function Practice
# Nov 24, 2023


def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> float:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


print(print_area_of_a_square(2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)



def stars(star_amount: float):
    for i in range(star_amount):
    	print("*")
        
print(stars(8))


numbs_response = 0
numbs = []
def biggest_of_three(biggest_numb: float,biggest_numb2: float, biggest_numb3: float) -> float:
    for i in range(3):
        numbs.append(input())
    for numb in input:
        if numb[0] > numb[1] and numb[0] > numb[2]:
            print(numb[1])
        if numb[1] > numb[2] and numb[1] > numb[2]:
            print(numb[2])
        if numb[2] > numb[0] and numb[2] > numb[1]:
            print(numb[3])
            

print(numbs)
            

	

          
