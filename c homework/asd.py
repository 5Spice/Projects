import random
import csv

# Deals a card. Values range from 1 to 10. Need to adjust j q k values to 10. Pop to remove and assign card value
def deal_card(card_deck):
    card_val = card_deck.pop(random.randint(0, len(card_deck)-1))
    return card_deck, card_val

card_deck = set_card_deck()
card_deck, card_val = deal_card(card_deck)
print("Drawn card: ", card_val)
print("Remaining card deck: ", card_deck)
    
    

    


# Handles the player's turn.  Returns the point value for the player's hand.
def get_score(card_deck):

    #assign point values for each card first
    def get_card_points(card_deck):
        card_val = {}
        for card in card_deck:
            card_name = card[0]
            player_val = int(card[1])
            card_val[card_name] = player_val
        return card_val   
    

    # Get the player's 

    player_val = 0
    
    player_val += card_val[player_card2.split()[0]]

    card_deck, player_val = deal_card(card_deck)
    # Get dealer's score.
    card_deck, dealer_val = deal_card(card_deck)
    # Get the player's score.
    card_deck, player_temp = deal_card(card_deck)
    player_val += player_temp
    # Get dealer's score.
    card_deck, dealer_temp = deal_card(card_deck)
    dealer_val += dealer_temp

    print("The sum of the first two cards is:", player_val)
    user_response = input("Do you want to take another card?: (Y/N)")

    ## you should display the sum of the two cards
    ## then, ask users whether they want to get another card
    ## if either the user is busted or the user wants to stop, then you need to stop
    while user_response == "Y" or user_response == "y":
        # Get the player's and dealer's score.

        ## Once you got the player_score, you have to check whether the player got busted and whether whether dealer got busted.
        ## If one of them got busted, return their scores immediately.


        ## ask user whether he/she wants to take another card
        user_response = input("Do you want to take another card?: (Y/N)")

    ## return the player and dealer's score
    return player_val, dealer_val

# Create a card deck from an input file (cards.txt).
# Then, return 52 cards saved in a list of lists
def set_card_deck():
    ## Complete this function

    return cards


# The main function.  It repeatedly plays games of blackjack until the user decides to stop.
def main():

    # Prime the loop and start the first game.
    user_response = "Y"
    while user_response == "Y" or user_response == "y":
        ## Set a card deck
        cards = set_card_deck()

        # Get the player's score.
        player_score, dealer_score = get_score( cards )

        ## Once you got the player_score and dealer_score, you have to check whether the player got busted, whether player's score
        ## is larger than the dealer's score. you also need to check the dealer's score.
        ## According to the result you should diaply different prompt.

        ## ask user whether he/she wants to play another game
        user_response = input("Do you want to play another game?: (Y/N)")


# Call the main function to start the blackjack program.
main()


