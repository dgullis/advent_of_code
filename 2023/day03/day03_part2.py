import re


class Star():
    def __init__(self, co_ordinates):
        self.co_ordinates = co_ordinates
        self.adjacent_numbers = []
    
    def adjacent_coordindates(self):
        row = self.co_ordinates[0]
        col = self.co_ordinates[1]
        return [(row, col+1), (row, col-1), 
                (row+1, col), (row-1, col), 
                (row+1, col+1), (row+1, col-1), 
                (row-1, col-1), (row-1, col+1)]

class Number():

    def __init__(self, value, co_ordinates):
        self.value = value
        self.co_ordinates = co_ordinates

class StarRepository():
    def __init__(self):
        self.stars = []
    
    def add_star(self, star):
        self.stars.append(star)
    
    def return_stars(self):
        return self.stars


class NumberRepository():

    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def return_numbers(self):
        return self.numbers
    

def find_stars_and_numbers():
    for line_idx, line in enumerate(lines):
        get_numbers_in_line(line, line_idx)
        get_stars_in_line(line, line_idx)
        
            
def get_numbers_in_line(line, line_index):
    pattern = re.compile(r'(\d+)')
    line_number_matches = pattern.finditer(line)
    for match in line_number_matches:
        co_ordinates = [(line_index, x) for x in range(match.start(), match.end())]
        new_number = Number(match.group(), co_ordinates)
        number_repository.add_number(new_number)

def get_stars_in_line(line, line_idx):
    pattern = re.compile(r'\*')
    star_match = pattern.finditer(line)
    for star in star_match:
        new_star = Star((line_idx, star.start()))
        star_repository.add_star(new_star)

def find_numbers_adjacent_to_stars(numbers, stars):
    for number in numbers:
        for star in stars:
            for num in number.co_ordinates:
                if num in star.adjacent_coordindates():
                    if number not in star.adjacent_numbers:
                        star.adjacent_numbers.append(number)

def calculate_sum_if_two_adjacent_nums(stars):
    sums_of_adjacenet_numbers = []
    for star in stars:
        if len(star.adjacent_numbers) == 2:
            sums_of_adjacenet_numbers.append(int(star.adjacent_numbers[0].value)*int( star.adjacent_numbers[1].value))

        if len(star.adjacent_numbers) == 4:
            sums_of_adjacenet_numbers.append(int(star.adjacent_numbers[2].value)*int( star.adjacent_numbers[3].value))
    return sums_of_adjacenet_numbers


with open('2023/day03/day03_input.txt', 'r') as file:
    lines = file.readlines()


star_repository = StarRepository()

number_repository = NumberRepository()

stars = star_repository.return_stars()

numbers = number_repository.return_numbers()

matching_numbers = find_stars_and_numbers()

find_numbers_adjacent_to_stars(numbers, stars)

sums_of_adj_nums = calculate_sum_if_two_adjacent_nums(stars)

result = sum(sums_of_adj_nums)
print(result)
