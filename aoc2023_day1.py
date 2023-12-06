import re
with open("./aoc2023_day1.txt") as f:
    for line in f:
        if line.strip():
            numbers = ''.join(filter(str.isdigit, f))
    print(numbers)






