# Kevin Chen
# 09/25/17
# This program is a game call blackjack, you will play with dealer as a player.


import random


def card():
    """
    This function represent the value of the card
    :return:random number between 1 to 10
    """
    number = random.randint(1, 10)
    return number


def main():
    card1 = card()
    card2 = card()
    player_total = card1 + card2

    print("your first card is", card1)
    print("your second card is", card2)
    print("and your total is", player_total)
    get_card = input("would you like another card?")
    if get_card in ["y", "Y", "yes"]:
        card3 = card()
        print("you drew a", card3)
        player_total = player_total + card3
        print("The total is", player_total)
    else:
        print("your total is", player_total)

    if player_total > 21:
        print("you lose")
    else:
        card4 = card()
        card5 = card()
        dealer_total = card4 + card5
        print("The dealer has", card4, "and", card5)
        print("The dealers total is", dealer_total)
        if player_total > dealer_total:
            print("you won")
        elif player_total == dealer_total:
            print("No one win this game")
        else:
            print("The dealer won")
main()
