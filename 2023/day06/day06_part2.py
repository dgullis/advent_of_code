import re


def get_time(puzzle):
    pattern = re.compile(r'Time:\s+([\d\s+]+)')
    time = pattern.findall(puzzle)
    time = int(''.join([time for time in time[0].split()]))
    return time

def get_distance(puzzle):
    pattern = re.compile(r'Distance:\s+([\d\s+]+)')
    distance = pattern.findall(puzzle)
    distance = int(''.join([distance for distance in distance[0].split()]))
    return distance

def get_number_ways_to_win(time, distance):
    ways_to_win = 0
    for i in range(0, time):
        competing_distance = i * (time-i)
        if competing_distance > distance:
            ways_to_win += 1
    return ways_to_win


with open("2023/day06/day06_input.txt", 'r') as f:
    puzzle = f.read()

time = get_time(puzzle)
distance = get_distance(puzzle)
result = get_number_ways_to_win(time, distance)

print(result)


