
import re

with open("2023/day05/day05_input.txt") as f:
    puzzle = f.read()


def get_seeds(puzzle):
    seed_pattern = re.compile(r'seeds: (\d\d.+)')
    seeds = seed_pattern.findall(puzzle)
    seeds = seeds[0].split()
    return seeds


def get_maps(puzzle, map_name):
    pattern = re.compile(f'{map_name} map:\s*([\d\s]+)')
    maps = pattern.findall(puzzle)
    maps = maps[0].split('\n')
    maps = [item.split() for item in maps if item]
    return maps


map_names = ['seed-to-soil', 
'soil-to-fertilizer', 
'fertilizer-to-water',
'water-to-light', 
'light-to-temperature', 
'temperature-to-humidity', 
'humidity-to-location']


def get_option_from_mapping(map, number):
    destination_range_start = int(map[0])
    source_range_start = int(map[1])
    range_length = int(map[2])
    if number > source_range_start + range_length:
        return number
    elif number >= source_range_start and number < source_range_start + range_length:
            return destination_range_start + (number - source_range_start)
    return number





def get_location(seed, puzzle):
    maps = [
        ('seed-to-soil', 'soil-to-fertilizer'),
        ('fertilizer-to-water', 'water-to-light'),
        ('light-to-temperature', 'temperature-to-humidity'),
        ('humidity-to-location', None) 
    ]

    current_value = seed
    for source_map, next_map in maps:
        current_value = get_option(puzzle, source_map, current_value)
        if next_map:
            current_value = get_option(puzzle, next_map, current_value)
        else:
            return current_value

def get_option(puzzle, map_type, value):
    maps = get_maps(puzzle, map_type)
    for mapping in maps:
        source_option = get_option_from_mapping(mapping, value)
        if source_option != value:
            return source_option
    return value


raw_seeds = [int(seed) for seed in get_seeds(puzzle)]


locations = 0

def seed_generator(raw_seeds):
    for i in range(0, len(raw_seeds), 2):
        for seed in range(raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]):
            yield seed

seed_gen = seed_generator(raw_seeds)

for seed in seed_gen:
    print(seed)
    location = get_location(seed, puzzle)
    if locations == 0:
        locations = location
    else:
        if location < locations:
            locations = location

result = locations
print('result', result)





# print('result: ', result)































