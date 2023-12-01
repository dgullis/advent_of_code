
import re

with open('input_files/day01_input.txt', 'r') as file:
    list_of_codes = file.readlines()

pattern = re.compile(r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))')
char_to_replace = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

lines_to_sum = []
for code in list_of_codes:
    matched_digits = pattern.findall(code)
    matched_digits = [char_to_replace.get(match, match) for match in matched_digits]
    if len(matched_digits) == 1:
        lines_to_sum.append(int(matched_digits[0] + matched_digits[0]))
    if len(matched_digits) >= 2:
        lines_to_sum.append(int(matched_digits[0] + matched_digits[-1]))
    
result = sum(lines_to_sum)
print(result)
