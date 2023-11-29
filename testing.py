

def bigest_of_three(biggest_numb: float, biggest_numb2: float, biggest_numb3: float):
    if biggest_numb > biggest_numb2 and biggest_numb > biggest_numb3:
        print(biggest_numb)
    if biggest_numb2 > biggest_numb and biggest_numb2 > biggest_numb3:
        print(biggest_numb2)
    if biggest_numb3 > biggest_numb and biggest_numb3 > biggest_numb2:
        print(biggest_numb3)



def pyramid(stars: int): 
    rows = 1
    for i in range(stars):
        for j in range(i + 1):
            print(end="*")
            
pyramid(5)
