import re


def get_times(puzzle):
    pattern = re.compile(r'Time:\s+([\d\s+]+)')
    times = pattern.findall(puzzle)
    times = [int(time) for time in times[0].split()]
    return times

def get_distances(puzzle):
    pattern = re.compile(r'Distance:\s+([\d\s+]+)')
    distances = pattern.findall(puzzle)
    distances = [int(distance) for distance in distances[0].split()]
    return distances

def get_number_ways_to_win(time, idx, distances):
        ways_to_win = []
        for i in range(0, time):
            competing_distance = i * (time-i)
            if competing_distance > distances[idx]:
                ways_to_win.append(competing_distance)
        return len(ways_to_win)

with open("2023/day06/day06_input.txt", 'r') as f:
    puzzle = f.read()


times = get_times(puzzle)
distances = get_distances(puzzle)

total = 0
for idx, time in enumerate(times):
    number_of_ways_to_win = get_number_ways_to_win(time, idx, distances)
    if not total:
        total = number_of_ways_to_win
    else:
        total *=number_of_ways_to_win

print(total)