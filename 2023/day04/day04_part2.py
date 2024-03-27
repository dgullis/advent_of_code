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

def check_cards_for_winning_numbers(cards):
    card_number_with_winning_numbers = []
    for card_idx, card in enumerate(cards): 
        card_number = card_idx+1
        winning_numbers_list, numbers_you_have_list = split_list(card)
        winning_numbers = get_numbers(winning_numbers_list)
        numbers_you_have = get_numbers(numbers_you_have_list)
        winning_numbers_you_have = check_numbers_against_cards(winning_numbers, numbers_you_have)
        card_number_with_winning_numbers.append([card_number, winning_numbers_you_have])
    return card_number_with_winning_numbers

def create_card_data_dict(card_numbers_with_winning_numbers):
    card_data_dict = {}
    for card in card_numbers_with_winning_numbers:
        card_number = card[0]
        quantity_matching_nums = len(card[1])
        card_data_dict[card_number] = {'matching_numbers': quantity_matching_nums ,
                                            'copies' : 1}
    return card_data_dict

def calculate_copies(card_data_dict):
    for card_number, matches in card_data_dict.copy().items():
        copies = matches.get('copies')
        for i in range(copies):
            for i in range(matches.get('matching_numbers')):
                card_data_dict[card_number+(i+1)]['copies'] +=1
    return card_data_dict

def calculate_result(dict_card_winning_nums_copies):
    result = 0
    for card_data in dict_card_winning_nums_copies.values():
        result += card_data['copies']
    return result




with open("2023/day04/day04_input.txt") as f:
    lines = f.readlines()

cards_with_winning_numbers = check_cards_for_winning_numbers(lines)
initial_card_data_dict = create_card_data_dict(cards_with_winning_numbers)
final_card_data_dict = calculate_copies(initial_card_data_dict)
result = calculate_result(final_card_data_dict)
print(result)
