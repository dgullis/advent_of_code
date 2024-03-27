import re

with open("2023/day08/day08_input.txt") as f:
    puzzle_lines = f.readlines()

directions = puzzle_lines[0].split()[0]
pattern = re.compile(r'[A-Z0-9]{3}')

def create_maps_dict(puzzle_lines, pattern):
    maps = {}
    for line in puzzle_lines[2:]:
        elements = pattern.findall(line)
        maps[elements[0]] = [elements[1], elements[2]]
    return maps

def get_elements_starting_with_a(maps):
    starting_elements = [element for element in maps.keys() if element[-1]=='A']
    return starting_elements





# def calculate_steps():
#     ending_elements = []
#     counter = 0
#     element = ''
#     for direction in directions:
#         if direction == 'R':
#             element = maps[element][1]
#         else:
#             element = maps[element][0]
#         if element[-1] != 'Z':
#             ending_elements.append(element[-1])
#         counter+=1
    
            


    

maps = create_maps_dict(puzzle_lines, pattern)
starting_elements = get_elements_starting_with_a(maps)
print(starting_elements)




def calculate_steps_to_last_letter_z(element, count):
    counter = count
    for direction in directions:
        if direction == 'R':
            element = maps[element][1]
        else:
            element = maps[element][0]
        counter += 1
        if element[-1] == 'Z':
            return counter

counts = []
elements = []
for element in starting_elements:
    count = calculate_steps_to_last_letter_z(element)
    counts.append(count)

common_numbers = set(counts[0])
for sublist in counts[1:]:
    common_numbers = common_numbers.intersection(set(sublist))

if common_numbers:
    lowest_common_number = min(common_numbers)
    print("Lowest common number:", lowest_common_number)
else:
    print("No common numbers found.")


#put each element throught the function
#returns steps until last letter 'Z' also returns that element

#checks if there is a LCM
#if not back pas back the last elements into the function
# count should start    
    

