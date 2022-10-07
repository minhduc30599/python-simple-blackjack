import random
import os

from art import logo

def clear():
    """Clear the console"""
    os.system('clear')

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

def calculate_score(cards_list):
    """Calculate card list"""
    cards_sum = sum(cards_list)

    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    elif cards_sum > 21:    
        for i in range(len(cards_list)):
            if cards_list[i] == 11:
                cards_list[i] = 1

            return sum(cards_list)
    else:
        return cards_sum

def compare(user_score, computer_score):
    if computer_score == 0:
        print('Computer win. BLACKJACK')
    elif user_score == 0:
        print('User win. BLACKJACK')
    elif computer_score > 21:
        print("Computer went over. You win")
    elif user_score > 21:
        print("You went over. Computer win")
    elif computer_score > user_score:
        print('Computer win')
    elif computer_score < user_score:
        print('User win')
    elif computer_score == user_score:
        print('Draw')

def play():
    """Play Blackjack"""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_end = False

    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_end:
        user_cards_sum = calculate_score(user_cards)
        computer_cards_sum = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_cards_sum == 0 or computer_cards_sum == 0 or user_cards_sum > 21:
            is_game_over = True
        else:
            get_another_card_or_not = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card_or_not == 'n':
                is_game_end = True
            elif get_another_card_or_not == 'y':
                user_cards.append(deal_card())

    while computer_cards_sum != 0 and computer_cards_sum < 17:
        computer_cards.append(deal_card())
        computer_cards_sum = calculate_score(computer_cards)

        print(f'Your final hand: {user_cards}')
        print(f"Computer's final hand: {computer_cards}")

        compare(user_cards_sum, computer_cards_sum)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play() 