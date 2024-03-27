import re

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

def calculate_section_max_boundary(maps):
    setion_max_boundary = 0
    for map in maps:
        max_boundary = int(map[1]) + int(map[2])
        if setion_max_boundary == 0 or setion_max_boundary < max_boundary:
            setion_max_boundary = max_boundary
    return max_boundary

def calculate_section_min_boundary(maps):
    section_min_boundary = 0
    for map in maps:
        min_boundary = int(map[1])
        if section_min_boundary == 0 or section_min_boundary > min_boundary:
            section_min_boundary = min_boundary
    return min_boundary


def get_next_location(maps, old_location):
    max_boundary = calculate_section_max_boundary(maps)
    min_boundary = calculate_section_min_boundary(maps)
    if old_location > max_boundary or old_location < min_boundary:
        return old_location
    for map in maps:
            destination_range_start = int(map[0])
            source_range_start = int(map[1])
            range_length = int(map[2])
            new_location = get_option(old_location,destination_range_start,source_range_start, range_length)
            if new_location != old_location:
                return new_location
    return old_location

def get_option(location, destination_range_start,source_range_start, range_length):
    if location >= source_range_start and location < source_range_start + range_length:
            return destination_range_start + (location - source_range_start)
    return location







with open("2023/day05/day05_input.txt") as f:
    puzzle = f.read()


raw_seeds = [int(seed) for seed in get_seeds(puzzle)]
print(raw_seeds)

seed_start = 0
for i in range(0, len(raw_seeds), 2):
    if seed_start == 0 or seed_start > raw_seeds[i]:
        seed_start = raw_seeds[i]

print(seed_start)

seed_end = 0

for i in range(0, len(raw_seeds), 2):
    if seed_end == 0 or seed_end < raw_seeds[i]+raw_seeds[i+1]:
        seed_end =  raw_seeds[i]+raw_seeds[i+1]

print(seed_end)


# for i in range(0, len(raw_seeds), 2):
#         for seed in range(raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]):


map_names = ['seed-to-soil', 
'soil-to-fertilizer', 
'fertilizer-to-water',
'water-to-light', 
'light-to-temperature', 
'temperature-to-humidity', 
'humidity-to-location']


def process_seeds():
    final_location = 0

    for seed in range(seed_start, seed_end):
        print(seed)
        new_option = seed
        for map_name in (map_names):
            maps = get_maps(puzzle, map_name)
            location = get_next_location(maps, new_option)
            new_option=location
        if final_location == 0 or final_location > location:
            final_location = location
    return final_location

result = process_seeds()
print(result)
