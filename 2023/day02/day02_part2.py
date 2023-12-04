import re

with open('2023/day02/day02_input.txt', 'r') as f:
    list_of_games = f.readlines()

blue_pattern = re.compile(r'(\d+)\sblue')
green_pattern = re.compile(r'(\d+)\sgreen')
red_pattern = re.compile(r'(\d+)\sred')

power_of_lines = []
for game in list_of_games:
    max_blue_cubes = max([int(cubes) for cubes in blue_pattern.findall(game)])
    max_green_cubes = max([int(cubes) for cubes in green_pattern.findall(game)])
    max_red_cubes = max([int(cubes) for cubes in red_pattern.findall(game)])
    power_of_line = max_blue_cubes * max_green_cubes * max_red_cubes
    power_of_lines.append(power_of_line)

result = sum(power_of_lines)
print(result)

