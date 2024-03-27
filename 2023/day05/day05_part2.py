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

map_names = ['seed-to-soil', 
'soil-to-fertilizer', 
'fertilizer-to-water',
'water-to-light', 
'light-to-temperature', 
'temperature-to-humidity', 
'humidity-to-location']


def get_next_location(maps, old_location):
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
print(raw_seeds)

min_seed_range = 0
for i in range(0, len(raw_seeds), 2):
    if not min_seed_range:
        min_seed_range = raw_seeds[i]
    if min_seed_range > raw_seeds[i]:
        min_seed_range = raw_seeds[i]


max_seed_range = 0
for i in range(0, len(raw_seeds), 2):
    range_check = raw_seeds[i] + raw_seeds[i+1]
    if not max_seed_range:
        max_seed_range = range_check
    if max_seed_range < range_check:
        max_seed_range = range_check

total_seed_range = (min_seed_range, max_seed_range)

for i in range(40000000, 40867799):
    next_location = i
    for map in reversed(map_names):
        maps = get_maps(puzzle, map)
        next_location = get_next_location(maps, next_location)
    if min_seed_range <= next_location <= max_seed_range:
        print(i)
        print(next_location)
        break
print("finish")


    


#reverse map names
#get maps within map_names
#get next location



