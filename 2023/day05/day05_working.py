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
    # max_boundary = calculate_section_max_boundary(maps)
    # min_boundary = calculate_section_min_boundary(maps)
    # if old_location > max_boundary or old_location < min_boundary:
    #     return old_location
    for map in maps:
            destination_range_start = int(map[0])
            source_range_start = int(map[1])
            range_length = int(map[2])
            new_location = get_option(old_location,destination_range_start,source_range_start, range_length)
            if new_location != old_location:
                return new_location
    return old_location

def get_option(location, destination_range_start,source_range_start, range_length):
    if location >= destination_range_start and location < destination_range_start + range_length:
            return location + (source_range_start-destination_range_start)
    return location



with open("2023/day05/day05_input.txt") as f:
    puzzle = f.read()

raw_seeds = [int(seed) for seed in get_seeds(puzzle)]



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





map_names = ['seed-to-soil', 
'soil-to-fertilizer', 
'fertilizer-to-water',
'water-to-light', 
'light-to-temperature', 
'temperature-to-humidity', 
'humidity-to-location']

# for i in range(0, len(raw_seeds), 2):




def process_seeds():
    for end_location in range(40867800, 9999999999, 1000):
        print(end_location)
        final_location_to_return = end_location
        for map_name in reversed(map_names):
            maps = (get_maps(puzzle, map_name))
            # print(maps)
            location = get_next_location(maps, end_location)
            end_location=location
        if seed_start <= end_location <= seed_end:
            return final_location_to_return

result = process_seeds()
print("result =" , result)
