import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def number(draw_cards):
    draw_cards = []
    for number in range(2):
        draw = random.choice(cards)
        draw_cards.append(draw)
    return draw_cards

player = number(cards)
dealer = number(cards)

print(art.logo)
print(f"Your cards: {player}")
print(f"Dealer's first card: {dealer[0]}")

player_summation = 0
for card in player:
    player_summation += card

dealer_summation = 0
for card in dealer:
    dealer_summation += card

hit = True
while hit:
    player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if player_choice[0] == "y":
        draw = random.choice(cards)
        player.append(draw)
        player_summation += player[-1]
        print(f"Your hand {player}")
        if player_summation >= 21:
            hit = False
    if dealer_summation <= 18:
        draw = random.choice(cards)
        dealer.append(draw)
        dealer_summation += dealer[-1]
        if dealer_summation > 21:
            hit = False
    else:
        hit = False
        
print(f"Your final hand: {player} = {player_summation}")
print(f"Computer final hand: {dealer} = {dealer_summation}")

if player_summation > dealer_summation and player_summation <= 21:
    print("You win!")
elif player_summation == dealer_summation:
    print("Draw")
else:
    print("You lose!")

##################### Hints #####################

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

