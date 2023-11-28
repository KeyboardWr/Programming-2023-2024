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


numbs = []
def bigest_of_three(biggest_numb: float, biggest_numb2: float, biggest_numb3: float):
    if biggest_numb > biggest_numb2 and biggest_numb > biggest_numb3:
        print(biggest_numb)
    elif biggest_numb2 > biggest_numb and biggest_numb2 > biggest_numb3:
        print(biggest_numb2)
    elif biggest_numb3 > biggest_numb and biggest_numb3 > biggest_numb2:
        print(biggest_numb3)
            

bigest_of_three(100,200,300)
            

            


def half_pyramid(rows):
    print("*")
    for i in range(1, rows + 1):
        print('* ' * i)

half_pyramid(5)

        
            

	

          
