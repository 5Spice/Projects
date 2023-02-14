def set_card_deck():
    card_deck = []
    with open(r"c:\Users\steve\OneDrive\Projects\c homework\123.txt", "r") as file:
        for line in file:
            card = line.strip().split(",")
            card_deck.append(card)
    return card_deck

card_deck = set_card_deck()
print(card_deck)