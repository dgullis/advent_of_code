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
    maps = [[int(num) for num in map] for map in maps]
    return maps

map_names = ['seed-to-soil', 
'soil-to-fertilizer', 
'fertilizer-to-water',
'water-to-light', 
'light-to-temperature', 
'temperature-to-humidity', 
'humidity-to-location']

with open("2023/day05/day05_input.txt") as f:
    puzzle = f.read()

seeds = get_seeds(puzzle)
seeds = list(map(int, seeds))

list_of_maps = []
for map in map_names:
    list_of_maps.append(get_maps(puzzle, map))


class Map:
    def __init__(self, maps):
        self.rules = []
        for m in maps:
            dest, source, size = m
            self.rules.append((dest, source, size))

    def convert(self, input):
        for dest, source, size in self.rules:
            if source <= input < source+size:
                return dest + input-source
        return input

def get_location(seed, maps):
    for m in maps:
        seed = m.convert(seed)
    return seed

maps = [Map(maps) for maps in list_of_maps]

def run(seeds, maps):
    locations = []
    for seed in seeds:
        location = get_location(seed, maps)
        locations.append(location)
    return min(locations)

result = run(seeds, maps)
print(result)
    






