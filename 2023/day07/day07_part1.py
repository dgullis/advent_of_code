import functools


class Hand():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.value = 0
        self.rank = 0

    def calculate_hand_value(self):
        card_quantity_dict = self.get_how_many_of_each_card(self.cards)
        # print('card_quant_dict: ', card_quantity_dict)
        
        length = len(card_quantity_dict)
        # print('lenght of dict: ', length)
        if length == 5:
            self.value = 1
        elif length == 4:
            self.value = 2
        elif length == 3:
            if max([q for q in card_quantity_dict.values()]) == 2:
                self.value = 3
            else: self.value = 4
        elif length == 2:
            if max([q for q in card_quantity_dict.values()]) == 3:
                self.value = 5
            else: self.value = 6
        else:
            self.value = 7

    def get_how_many_of_each_card(self, cards):
        card_times = {}
        for card in cards:
            if card not in card_times:
                card_times[card] = 1
            else:
                card_times[card] += 1
        return card_times



class HandOrganiser():
    def __init__(self):
        self.hands = []
    
    def add_hand(self, hand):
        self.hands.append(hand)
    
    def return_all_hands(self):
        return self.hands
    
    def return_hand_hierarchy(self):
        pass



                    

with open('/Users/dangullis/Desktop/Projects/advent_of_code/2023/day07/day07_test_input.txt', 'r') as f:
    puzzle_lines = f.readlines()

hand_organiser = HandOrganiser()

def get_hands_and_bids_from_puzzle(puzzle_lines):
    hands_and_bids = {}
    for puzzle in [puzzle.split() for puzzle in puzzle_lines]:
        hands_and_bids[puzzle[0]] = puzzle[1]
    return hands_and_bids

def compare_hands_return_lower(hand1, hand2):
    cards_and_values = {'A':13,'K':12,'Q':11,'J':10,'T':9,'9':8,'8':7,'7':6,'6':5, 
                    '5':4,'4':3,'3':2,'2':1}
    idx = 0
    if hand1.value < hand2.value:
        return hand1
    elif hand2.value < hand1.value:
        return hand2
    
    elif hand1.value == hand2.value:
        while cards_and_values[hand1.cards[idx]] == cards_and_values[hand2.cards[idx]]:
            idx+=1
        else:
            if cards_and_values[hand1.cards[idx]] < cards_and_values[hand2.cards[idx]]:
                return hand1
            else:
                return hand2


def custom_sort(lst, compare_hands_return_lower):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            result = compare_hands_return_lower(lst[j], lst[j+1])
            if result != lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


hands_and_bids = get_hands_and_bids_from_puzzle(puzzle_lines)

for hand, bid in hands_and_bids.items():
    hand = Hand([card for card in hand], bid)
    hand_organiser.add_hand(hand)

for hand in hand_organiser.return_all_hands():
    hand.calculate_hand_value()


list_of_hands = [hand for hand in hand_organiser.return_all_hands()]


sorted_hands = custom_sort(list_of_hands,compare_hands_return_lower)

for idx, hand in enumerate([hand for hand in sorted_hands]):
    hand.rank = idx+1

total_winnings = 0

for hand in sorted(hand_organiser.return_all_hands(), key=lambda x: x.rank):
    total_winnings += (hand.bid*hand.rank)

print(total_winnings)


