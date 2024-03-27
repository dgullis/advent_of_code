import re

def split_list(list):
    split_list =list.split('|')
    winning_numbers_list = split_list[0]
    winning_numbers_list = winning_numbers_list.split(":")[1]
    numbers_you_have_list = split_list[1]
    return winning_numbers_list, numbers_you_have_list

def get_numbers(list):
    pattern = re.compile(r'\d+')
    numbers = pattern.findall(list)
    return numbers

def check_numbers_against_cards(winning_numbers, numbers_to_check):
    numbers_in_cards = []
    for number in numbers_to_check:
        if number in winning_numbers:
            numbers_in_cards.append(number)
    return numbers_in_cards

def get_points(winning_numbers_you_have):
    if not winning_numbers_you_have:
        return 0
    elif len(winning_numbers_you_have) == 1:
        points = 1
        return points
    else:
        points = 2**(len(winning_numbers_you_have)-1)
        return points

with open("2023/day04/day04_input.txt") as f:
    lines = f.readlines()

    
    
    game_points = 0
for line in lines:  
    winning_numbers_list, numbers_you_have_list = split_list(line)
    winning_numbers = get_numbers(winning_numbers_list)
    numbers_you_have = get_numbers(numbers_you_have_list)
    winning_numbers_you_have = check_numbers_against_cards(winning_numbers, numbers_you_have)
    game_points += get_points(winning_numbers_you_have)

print(game_points)
    
    
