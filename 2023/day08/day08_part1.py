import re

with open("2023/day08/day08_input.txt") as f:
    puzzle_lines = f.readlines()

directions = puzzle_lines[0].split()[0]
pattern = re.compile(r'[A-Z]{3}')
def create_maps_dict(puzzle_lines, pattern):
    maps = {}
    for line in puzzle_lines[2:]:
        elements = pattern.findall(line)
        maps[elements[0]] = [elements[1], elements[2]]
    return maps

def calculate_steps_to_last_letter_z(element):
    counter = 0
    while True:
        for direction in directions:
            if direction == 'R':
                element = maps[element][1]
            else:
                element = maps[element][0]
            counter += 1
            if element[-1] == 'Z':
                return counter
    

maps = create_maps_dict(puzzle_lines, pattern)
count = calculate_steps_to_last_letter_z()


print(count)


