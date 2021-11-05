#Alex Maximilian github.com/Alexmaximillian
#Simple Blackjack game inspired by other repos
#Enjoy

import os
import random

decks = input("Enter the number of decks you want to play with: ")

#Sets up the  cards
deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*(int(decks)*4)

#Initialise the scores
wins = 0
losses = 0

#Add money system associated with wins and losses
balance = 1000

def thedeal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card) #Took the card from the deck removed it with pop and added it to hand
    return hand

print(thedeal(deck))
print(deck)

def keep_playing():
    keep = input("Would you like to keep playing Blackjack? (Y/N) : ")
    if keep == "y" or "Y" or "yes" or "Yes" or "ye" "Ye":
        dealer_hand = []
        player_hand = []
        deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        #play game
    else:
        print("Thank you for playing at Alex's Blackjack table, your final balance is", str(balance))
        quit()

def totalhand(hand):
    totalhand = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            totalhand+= 10
        elif card == "A": #This makes its so that card 14 or the ace is either a 1 or an 11 depending on the totalhand
            if totalhand >= 11: totalhand+= 1
            else: totalhand+= 11
        else: totalhand += card
    return totalhand

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def showing_results(dealer_hand, player_hand):
    clear()

    
    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(totalhand(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(totalhand(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if totalhand(player_hand) == 21:
        showing_results(dealer_hand, player_hand)
        print ("Congratulations sir! You got a Blackjack!\n")
        wins += 1
        keep_playing()
    elif totalhand(dealer_hand) == 21:
        showing_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        keep_playing()


