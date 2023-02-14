import csv
import random 
# Deals a card. Values range from 1 to 10. Need to adjust j q k values to 10. Pop to remove and assign card value
def deal_card(card_deck):
    card_val = card_deck.pop(random.randint(0, len(card_deck)-1))
    return card_deck, card_val


    
def set_card_deck():
    card_deck = []
    with open(r"c:\Users\steve\OneDrive\Projects\c homework\123.txt", "r") as file:
        reader = csv.reader(file)
        card_deck = list(reader)
    for i in range(len(card_deck)):
        if card_deck[i][0] in ['J','Q','K']:
            card_deck[i][0] = '10'
    return card_deck

card_deck = set_card_deck()
print(card_deck)
card_deck = set_card_deck()
card_deck, card_val = deal_card(card_deck)
print("Drawn card: ", card_val)
print("Remaining card deck: ", card_deck)