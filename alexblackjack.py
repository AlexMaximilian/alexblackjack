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





