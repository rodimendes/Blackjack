import art
import random
import replit

def number(draw_cards):
    draw_cards = []
    for number in range(2):
        draw = random.choice(cards)
        draw_cards.append(draw)
    return draw_cards

def summation(cards_list):
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        print(cards_list)
        cards_list.append(1)
        print(cards_list)
        print(sum(cards_list))
    return sum(cards_list)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True
while play:
    play = input("Do you want to play? 'y' to yes or 'n' to exit\n").lower()
    if play[0] == 'n':
        play = False
    else:
        replit.clear()
        player = number(cards)
        dealer = number(cards)

        print(art.logo)
        print(f"Your cards: {player}")
        print(f"Dealer's first card: {dealer[0]}")

        player_summation = summation(player)
        dealer_summation = summation(dealer)

        hit = True
        while hit:
            player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if player_choice[0] == "y":
                draw = random.choice(cards)
                player.append(draw)
                player_summation = summation(player)
                print(f"Your hand {player}")
                if player_summation >= 21:
                    hit = False
            else:
                hit = False

        while dealer_summation <= 18:
            draw = random.choice(cards)
            dealer.append(draw)
            dealer_summation = summation(dealer)

        if player_summation > 21:
            print(f"Your final hand: {player} = {player_summation}")
            print("You lose!")
        elif dealer_summation > 21:
            print(f"Computer final hand: {dealer} = {dealer_summation}")
            print("You win!")
        elif player_summation > dealer_summation and player_summation <= 21:
            print(f"Your final hand: {player} = {player_summation}")
            print(f"Computer final hand: {dealer} = {dealer_summation}")
            print("You win!")
        elif dealer_summation > player_summation and dealer_summation <= 21:
            print(f"Your final hand: {player} = {player_summation}")
            print(f"Computer final hand: {dealer} = {dealer_summation}")
            print("You lose!")
        else:
            print(f"Your final hand: {player} = {player_summation}")
            print(f"Computer final hand: {dealer} = {dealer_summation}")
            print("Draw")

