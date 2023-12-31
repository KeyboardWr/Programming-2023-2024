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



def stars(numb_stars: int) -> str:

    return "*" * numb_stars

print(stars(5))
        


numbs = []
def bigest_of_three(biggest_numb: float, biggest_numb2: float, biggest_numb3: float):
    if biggest_numb > biggest_numb2 and biggest_numb > biggest_numb3:
        print(biggest_numb)
    elif biggest_numb2 > biggest_numb and biggest_numb2 > biggest_numb3:
        print(biggest_numb2)
    elif biggest_numb3 > biggest_numb and biggest_numb3 > biggest_numb2:
        print(biggest_numb3)
            

bigest_of_three(100,200,300)
            

            


def pyramid(rows: int) -> None:
    for current_layer in range(1, rows + 1):
        print(stars(current_layer))
pyramid(5)


def pyramid_mirror(numb_layers: int) -> None:
    for current_layer in range(1, numb_layers + 1):
        spaces = " " * (numb_layers - current_layer)
        print(spaces + stars(current_layer))

pyramid_mirror(5)


def linear_search(l: list, item: any) -> int:
    """Search through a list and if found,
    returns the index of the first occurence
    of the item.

    Params:
            l - list we're search through
            item - item we're looking for

    Returns:
            index if found, -1 if not found
    """
    counter = 0

    # search algorithm
    for thing in l:
        if thing == item:
            return counter
        counter += 1

    return -1


pockets = ["coins", "lint", "paperclip", "keys", "wallet"]

results = linear_search(pockets, "keys")

if results == -1:
    print("Your keys are not in your pockets")
else:
    print(f"Found your keys! They're in the {results}th index.")
            

	

          
