import random

DECK_OF_CARDS_SUITES = ['♥', '♠', '♦', '♣']
DECK_OF_CARD_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random_suites, random_cards, your_hand = [], [], []
SCORE = ['Straight Flush',
         'Four of a Kind',
         'Full House',
         'Flush',
         'Straight',
         'Three of a kind',
         'Two Pair',
         'One Pair',
         'High Card']


def draw():
    for index in range(5):
        random_suites.append('{}'.format(random.choice(DECK_OF_CARDS_SUITES)))
        random_cards.append('{}'.format(random.choice(DECK_OF_CARD_CARDS)))
        your_hand.append('{}{}'.format(random_suites[index], random_cards[index]))


def search_for_something_straightish_decorator(func):
    def wrapper():
        if len(set(random_suites)) == 1 and len(random_cards) == len(set(random_cards)):
            result = func()
            if result == None:
                return result
            return SCORE[0]
        elif len(set(random_suites)) != 1 and len(random_cards) == len(set(random_cards)):
            result = func()
            if result == None:
                return result
            return SCORE[4]
    return wrapper


@search_for_something_straightish_decorator
def search_for_something_straight():
    score = SCORE[8]
    DECK_OF_CARDS_RE_ARRANGED = DECK_OF_CARD_CARDS[8::] + DECK_OF_CARD_CARDS[0:8]
    for index in range(len(DECK_OF_CARD_CARDS)):
        sub_list_one = DECK_OF_CARD_CARDS[index:index + 5]
        sub_list_two = DECK_OF_CARDS_RE_ARRANGED[index:index + 5]
        if all(element in sub_list_one for element in random_cards):
            return score
        elif all(element in sub_list_two for element in random_cards):
            return score
    return None


def straight_flush():
    result = search_for_something_straight()
    return result


def four_of_a_kind():
    if len(set(random_suites)) != 1:
        for element in random_cards:
            if random_cards.count(element) == 4:
                return SCORE[1]


def full_house():
    add_up = 0
    for element in random_cards:
        if random_cards.count(element) == 2 or random_cards.count(element) == 3:
            add_up += 1
    if add_up == 5:
        return SCORE[2]


def flush():
    if len(set(random_suites)) == 1:
        return SCORE[3]


def straight():
    result = search_for_something_straight()
    return result


def three_of_a_kind():
    add_up = 0
    if len(set(random_suites)) != 1:
        for element in random_cards:
            if random_cards.count(element) == 3:
                add_up += 1
        if add_up == 3:
            return SCORE[5]


def two_pair():
    add_up = 0
    f_house = full_house()
    if len(set(random_suites)) != 1:
        for element in random_cards:
            if random_cards.count(element) == 2:
                add_up += 1
        if add_up == 4 and f_house is None:
            return SCORE[6]


def one_pair():
    add_up = 0
    if len(set(random_suites)) != 1:
        for element in random_cards:
            if random_cards.count(element) == 2:
                add_up += 1
        if add_up == 2:
            return SCORE[7]


def high_card():
    return SCORE[8]


def main():
    function_list = [straight_flush,
                     four_of_a_kind,
                     full_house,
                     flush,
                     straight,
                     three_of_a_kind,
                     two_pair,
                     one_pair,
                     high_card]
    draw()
    print(f'Your hand is: {your_hand}')

    for function in function_list:
        func = function()
        if func == None:
            continue
        print(func)
        break


if __name__ == '__main__':
    main()

