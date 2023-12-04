import re

with open('2023/day02/day02_input.txt', 'r') as f:
    list_of_games = f.readlines()

blue_pattern = re.compile(r'(\w+)\sblue')
green_pattern = re.compile(r'(\w+)\sgreen')
red_pattern = re.compile(r'(\w+)\sred')

suitable_lines = []
for game in list_of_games:
    blue_cubes =  blue_pattern.findall(game)
    green_cubes = green_pattern.findall(game)
    red_cubes = red_pattern.findall(game)

    if all(int(cubes) <= 12 for cubes in red_cubes) and \
        all(int(cubes) <= 13 for cubes in green_cubes) and \
            all(int(cubes) <= 14 for cubes in blue_cubes):
        suitable_lines.append(list_of_games.index(game)+1)

result = sum(suitable_lines)
print(result)
    
