import re
from multiprocessing import Pool


# # for name in map_names:
# #     print(get_maps(puzzle, name))

# def get_source_and_destination_ranges(map):
#         destination_range_start = int(map[0])
#         source_range_start = int(map[1])
#         range_length = int(map[2])
#         destination_range = [i for i in range(destination_range_start, destination_range_start+range_length)]
#         source_range = [i for i in range(source_range_start, source_range_start+range_length)]
#         return source_range, destination_range



# def find_destination_from_source(source, source_range, destination_range):
#     if source in source_range:
#         destination = destination_range[source_range.index(source)]
#     else:
#         destination = source
#     return destination

# def calculate_destination(source, list_destinations):
#     if not list_destinations:
#         source = source
#     elif len(list_destinations) == 1:
#         source = list_destinations[0]
#     else:
#         source = min([(destination, abs(source-destination)) for destination in list_destinations], key=lambda x:x[1])[0]
#     return source

# def seed_generator(raw_seeds):
#     for i in range(0, len(raw_seeds), 2):
#         for seed in range(raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]):
#             yield seed



# def get_soil_location(seed):
#     maps = get_maps(puzzle, 'seed-to-soil')
#     for map in maps:
#         source_option = get_option(map, seed)
#         if source_option != seed:
#             return source_option
#     return seed

# def get_fertilizer(soil):
#     maps = get_maps(puzzle, 'soil-to-fertilizer')
#     for map in maps:
#         source_option = get_option(map, soil)
#         if source_option != soil:
#             return source_option
#     return soil

# def get_water(fertilizer):
#     maps = get_maps(puzzle, 'fertilizer-to-water')
#     for map in maps:
#         source_option = get_option(map, fertilizer)
#         if source_option != fertilizer:
#             return source_option
#     return fertilizer

# def get_light(water):
#     maps = get_maps(puzzle, 'water-to-light')
#     for map in maps:
#         source_option = get_option(map, water)
#         if source_option != water:
#             return source_option
#     return water

# def get_temp(light):
#     maps = get_maps(puzzle, 'light-to-temperature')
#     for map in maps:
#         source_option = get_option(map, light)
#         if source_option != light:
#             return source_option
#     return light

# def get_humidity(temp):
#     maps = get_maps(puzzle, 'temperature-to-humidity') 
#     for map in maps:
#         source_option = get_option(map, temp)
#         if source_option != temp:
#             return source_option
#     return temp

# # def get_location(humidity):
# #     maps = get_maps(puzzle, 'humidity-to-location') 
# #     for map in maps:
# #         source_option = get_option(map, humidity)
# #         if source_option != humidity:
# #             return source_option
# #     return humidity








# def calculate_max_source_boundary(maps):
#     max_boundary = 0
#     for map in maps:
#         if max_boundary == 0:
#             max_boundary = int(map[1]) + int(map[2])
#         else:
#             if int(map[1]) + int(map[2]) > max_boundary:
#                 max_boundary = int(map[1]) + int(map[2])
#     return max_boundary




# def get_maps(puzzle, map_name):
#     pattern = re.compile(f'{map_name} map:\s*([\d\s]+)')
#     maps = pattern.findall(puzzle)
#     maps = maps[0].split('\n')
#     maps = [item.split() for item in maps if item]
#     return maps


# ______________________



with open("2023/day05/day05_input.txt") as f:
    puzzle = f.read()


def seed_generator(raw_seeds):
    for i in range(0, len(raw_seeds), 2):
        for seed in range(raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]):
            yield seed

def generate_seeds(start, end):
    for seed in range(start, end):
        yield seed


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

def get_option(number, destination_range_start,source_range_start, range_length):
    if number >= source_range_start and number < source_range_start + range_length:
            return destination_range_start + (number - source_range_start)
    return number


map_names = ['seed-to-soil', 
'soil-to-fertilizer', 
'fertilizer-to-water',
'water-to-light', 
'light-to-temperature', 
'temperature-to-humidity', 
'humidity-to-location']

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



def get_next_location(maps, old_option):
    max_boundary = calculate_section_max_boundary(maps)
    min_boundary = calculate_section_min_boundary(maps)
    if old_option > max_boundary or old_option < min_boundary:
        return old_option
    for map in maps:
            destination_range_start = int(map[0])
            source_range_start = int(map[1])
            range_length = int(map[2])
            option = get_option(old_option,destination_range_start,source_range_start, range_length)
            if option != old_option:
                return option
    return old_option

def calculate_max_max_boundary(puzzle, map_names):
    max_boundary = 0
    for map_name in map_names:
        for map in get_maps(puzzle, map_name):
            if max_boundary == 0 or max_boundary < int(map[1]) + int(map[2]):
                max_boundary = int(map[1]) + int(map[2])
    return max_boundary

def calculate_min_boundary(puzzle, map_names):
    min_boundary = 0
    for map_name in map_names:
        for map in get_maps(puzzle, map_name):
            if min_boundary == 0 or min_boundary > int(map[2]):
                min_boundary = int(map[2])
    return min_boundary

def split_range(raw_seeds, chunk_size):
    seed_ranges = []
    for i in range(0, len(raw_seeds), 2):
        start = raw_seeds[i]
        end = start + raw_seeds[i + 1]
        seed_ranges.append((start, end))
    
    return [seed_ranges[i:i+chunk_size] for i in range(0, len(seed_ranges), chunk_size)]

max_boundary = calculate_max_max_boundary(puzzle, map_names)
min_boundary = calculate_min_boundary(puzzle, map_names)


# print(1347583290 < min_boundary)

def process_seeds(seed_range):
    final_location = 0
    for start, end in seed_range:
        seeds = list(generate_seeds(start, end))
        for seed in seeds:
            print(seed)
            new_option = seed
            for map_name in (map_names):
                    if new_option > max_boundary or new_option < min_boundary:
                        if final_location == 0 or final_location > location:
                            final_location = location
                    else:
                        maps = get_maps(puzzle, map_name)
                        location = get_next_location(maps, new_option)
                        new_option=location
            if final_location == 0 or final_location > location:
                final_location = location
    return final_location



# if __name__ == "__main__":
#     raw_seeds = [int(seed) for seed in get_seeds(puzzle)]
#     chunk_size = 9  # Example chunk size for splitting
    
#     seed_ranges = split_range(raw_seeds, chunk_size)
    
#     with Pool() as pool:
#         results = pool.map(process_seeds, seed_ranges)
#         print("results" , results)
                        
    




# def get_location(seed, puzzle):
#     maps = [
#         ('seed-to-soil', 'soil-to-fertilizer'),
#         ('fertilizer-to-water', 'water-to-light'),
#         ('light-to-temperature', 'temperature-to-humidity'),
#         ('humidity-to-location', None) 
#     ]

#     current_value = seed
#     for source_map, next_map in maps:
#         current_value = get_option(source_map, current_value)
#         if next_map:
#             current_value = get_option(next_map, current_value)
#         else:
#             return current_value













