from art import logo
from copy import deepcopy as dc
import random
from replit import clear

deck = {
    'total': 54,
    'stack': {'J': 4, 'K': 4, 'Q': 4, 'A': 4, 'L': 2, '10': 4, '9': 4, '8': 4, '7': 4, '6': 4, '5': 4, '4': 4, '3': 4,
              '2': 4},
    'cards': {
        'options': ['J', 'K', 'Q', 'A', 'L', '10', '9', '8', '7', '6', '5', '4', '3', '2'],
        'groups': {
            'letters': ['J', 'K', 'Q', 'A', 'L'],
            'numbers': ['10', '9', '8', '7', '6', '5', '4', '3', '2']
        },
        'values': {'J': 10, 'K': 10, 'Q': 10, 'A': [1, 11], 'L': 2, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
                   '4': 4, '3': 3,
                   '2': 2},
    }
}


def draw_card(pack, player):
    """to deal a card to a given player from the deck"""
    card = ''
    while True:
        pick = random.choice(pack['cards']['options'])
        if pack['stack'][pick] != 0:
            card = pick
            pack['total'] -= 1
            pack['stack'][pick] -= 1
            break
    player.append(card)


def total(values, player):
    """the sum total of a player's hand at a given time"""
    player_total = 0
    for card in player:
        if card == 'A':
            player_total += 11
        else:
            player_total += values[card]
    if (player_total > 21) and ('A' in player):
        for _ in range(player.count('A')):
            player_total -= 10  # -11 + 1 = -10 ~~ changing the value of A from 11 to 1 in the player_total
            if player_total < 21:
                break
    return player_total


def output(deal_order, comp_total, user_total):
    """ to judge and pronounce the winner at a given moment"""
    def inner_output():
        if comp_total < user_total <= 21:
            print("You Win!")
        elif comp_total > 21 and user_total <= 21:
            print("You Win!")
        elif comp_total == user_total:
            print('It is a draw!')
        else:
            print('You lose!')

    if deal_order == 1:
        if comp_total > 21:
            print('You Win!')
            return
        else:
            inner_output()
            return
    else:
        if user_total > 21:
            print('You Lose!')
            return
        else:
            inner_output()
            return


def play():
    pack = dc(deck)
    print(logo)
    comp, user, comp_total, user_total = [], [], 0, 0
    print('Welcome to BlackJack / 21')
    deal_order = random.choice([1, 2])
    draw = input('Please enter "P" to be delt a card: ').upper()
    while True:
        clear()
        if draw == 'P':
            if pack['total'] <= 2:
                pack = dc(deck)

            def player_draw(name, player):
                draw_card(pack, player)
                print(f'{name} ==>', player)
                player_total = total(pack['cards']['values'], player)
                print(f'{name}_total', player_total)
                print('=>|-----------------------------------------------------------------|')
                return player_total

            if deal_order == 1:
                comp_total = player_draw('comp', comp)
                user_total = player_draw('user', user)
            else:
                user_total = player_draw('user', user)
                comp_total = player_draw('comp', comp)

            if (comp_total >= 21) or (user_total >= 21):
                output(deal_order, comp_total, user_total)
                break

        elif draw == 'X':
            output(deal_order, comp_total, user_total)
            break
        else:
            print('Wrong entry! Enter "P" or "X", please!')
        draw = input('Please enter "P" to deal another round or "X" for Final Scores: P/X ').upper()

    to_continue = input('Would you like to start another session? Y/N ').upper()
    if to_continue == 'Y':
        play()
    else:
        for _ in [comp, user, comp_total, user_total, pack, deal_order, draw]:
            del _
        return


play()
