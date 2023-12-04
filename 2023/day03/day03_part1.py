import re

special_chars = ['*', '#', '+', '$', "/", '%', '=', '@', '-', '%', '&']


def find_matching_numbers():
    matching_numbers = []
    
    for line_idx, line in enumerate(lines):
        line_number_matches = get_numbers_in_line(line)
        # line_star_matches = get_stars_in_line(line)
        # for line in line_star_matches:
        #     print(line)
        for match in line_number_matches:
            number = match.group()
            index_of_last_digit = match.end()-1
            index_of_first_digit = match.start()
            before_or_after = special_char_before_or_after(line, number, index_of_first_digit, index_of_last_digit)
            above_or_below = special_char_adjacent_above_below(line_idx, lines, number, index_of_first_digit, index_of_last_digit)
            if before_or_after:
                matching_numbers.append(before_or_after)
            elif above_or_below:
                matching_numbers.append(above_or_below)

    return matching_numbers

def sum_matching_numbers(matching_numbers):
    return sum([int(number) for number in matching_numbers])

def get_numbers_in_line(line):
    pattern = re.compile(r'(\d+)')
    line_number_matches = pattern.finditer(line)
    return line_number_matches

# list_of_numbers_with_coordinates = []

# def get_stars_in_line(line):
#     pattern = re.compile(r'.*')
#     line_star_matches = pattern.finditer(line)
#     return line_star_matches

def special_char_before_or_after(line, number, index_of_first_digit, index_of_last_digit):
    found_number = ''

    if number[0] != line[0]:
        if line[index_of_first_digit-1] in special_chars:
            found_number = number
    if number[-1] != line[-1]:
        if line[index_of_last_digit+1] in special_chars:
            found_number = number
    return found_number

def special_char_adjacent_above_below(line_index, lines, number, index_of_first_digit, index_of_last_digit):
    found_number = ''
    if line_index != 0:
        if lines[line_index-1][index_of_first_digit] in special_chars or \
            lines[line_index-1][index_of_last_digit] in special_chars or \
            lines[line_index-1][index_of_first_digit+1] in special_chars or \
            lines[line_index-1][index_of_first_digit-1] in special_chars or \
            lines[line_index-1][index_of_last_digit-1] in special_chars or \
            lines[line_index-1][index_of_last_digit+1] in special_chars:
                found_number = number
            
    if line_index != (len(lines)-1):
        
        if lines[line_index+1][index_of_first_digit] in special_chars or \
            lines[line_index+1][index_of_last_digit] in special_chars or \
            lines[line_index+1][index_of_first_digit+1] in special_chars or \
            lines[line_index+1][index_of_first_digit-1] in special_chars or \
            lines[line_index+1][index_of_last_digit-1] in special_chars or \
            lines[line_index+1][index_of_last_digit+1] in special_chars:
                found_number = number

    return found_number
            

with open('2023/day03/day03_test_input.txt', 'r') as file:
    lines = file.readlines()

matching_numbers = find_matching_numbers()
result = sum_matching_numbers(matching_numbers)
print(result)

class Number():

    def __init__(self, value, co_ordinates):
        self.value = value
        self.co_ordinates = co_ordinates

class NumberRepository():

    def __init__(self, numbers):
        self.number = numbers

class Star():
    def __init__(self, co_ordinates):
        self.co_ordinates = co_ordinates
    
    def adjacent_coorindates(self):
        row = self.co_ordinates[0]
        col = self.co_ordinates[1]
    

    


