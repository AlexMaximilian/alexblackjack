#Alex Maximilian github.com/Alexmaximilian
#Simple Blackjack game enhanced from other repos
#Enjoy

import os
import random

decks = input("Enter number of decks to use: ")

balance = int(input("How much money are you bringing to the table? (Minimum of 100€, only in multiples of a 100€\n"))
if balance >= 100:
    initbalance = balance
else:
    print("Please enter a valid input. Number must be greater than a hundred and a multiple of a 100s")
    exit()

multiplier = int(input("How many 100€ chips do you want to bet"))

# user chooses number of decks of cards to use
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# initialize scores
wins = 0
losses = 0


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    global balance
    multiplier = 0
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        multiplier = int(input("How many 100€ chips do you want to bet"))
        game()
    else:
        if balance < 0:
            print("You are in debt to the casino by", balance, "You must find a way to repay us or else...")
            exit()
        else:
            print("Thanks for playing at Alex's Blackjack table your final balance is", str(balance) + '€ you started with', str(initbalance) + '€')
            exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

#Function to 'hit', take another card from the pile
def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

#Clearing the console so the game looks cleaner
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    WELCOME TO ALEX'S BLACKJACK!\n")
    print("-"*35+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*35+"\n")
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    global balance
    global multiplier
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        balance+= 100 * multiplier
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        balance-= 100 * multiplier
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        #Score function now updates to global win/loss variables
        global wins
        global losses
        global balance
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Congratulations! You got a Blackjack!\n")
            balance+=100 * multiplier
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry, you lose. The dealer got a blackjack.\n")
            balance-=100 * multiplier
            losses += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry. You busted. You lose.\n")
            balance-=100 * multiplier
            losses += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Dealer busts. You win!\n")
            balance+=100 * multiplier
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
            balance-=100 * multiplier
            losses += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Congratulations. Your score is higher than the dealer. You win\n")
            balance+=100 * multiplier
            wins += 1

#Main game loop
def game():
    global wins
    global losses
    global balance
    choice = 0
    clear()
    print("\n    WELCOME TO ALEX'S BLACKJACK!\n")
    print("-"*35+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*35+"\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("The dealer is showing a " + str(dealer_hand[0]))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('You busted')
                balance-=100 * multiplier
                losses += 1
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Dealer busts, you win!')
                    balance+=100 * multiplier
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            print("Thanks for playing at Alex's Blackjack table your final balance is", str(balance) + '$ you started with', str(initbalance) + '€')
            quit=True
            exit()

#Is used to execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
   game()
