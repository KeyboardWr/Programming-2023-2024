# AOC Day 1
# Herman Li
# November 30, 2023


elves = []

with open("./aoc2022day1.txt") as f:
    current_cals = 0
    for line in f:
        # If there is something in the line
        if line.strip():
            current_cals += int(line.strip())
        else:
            # Dump current_cals into elves list
            elves.append(current_cals)
            # Reset current_cals for next elf
            current_cals = 0

# find the biggest calories
biggest_cals = 0
for elf in elves:
    if elf > biggest_cals:
        biggest_cals = elf
print(biggest_cals)




# Get the top three and sum them
print(sum(sorted(elves)[-3:]))



