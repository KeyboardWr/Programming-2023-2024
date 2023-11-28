

def biggest_of_three(biggest_numb: float, biggest_numb2: float, biggest_numb3: float) -> float:
    if biggest_numb > biggest_numb2 and biggest_numb > biggest_numb3:
        print(biggest_numb)
    if biggest_numb2 > biggest_numb and biggest_numb2 > biggest_numb3:
        print(biggest_numb2)
    if biggest_numb3 > biggest_numb and biggest_numb3 > biggest_numb2:
        print(biggest_numb3)

biggest_of_three(2,3,5)