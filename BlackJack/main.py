from card import *
from deck import *
from handTests import *
from bjhand import *
import game

def dealHand(deck):
    """deals starting hands (2 cards) for 2 players. takes a deck and
    returns a tuple with the player's and dealer's hands"""
    hand = BJHand()
    hand.fillHand(2, deck)
    return hand

def displayHandAndScore(hand, whichPlayer):
    """displays a hand and its score. takes a hand and a string specifying the user"""
    print(f"{whichPlayer}'s hand:")
    print(f"{hand}")
    print(f"{whichPlayer}'s score: {hand.score()}")

def getAnotherCard():
    """asks the user if they want another card and validates answer"""
    from validation import getYesOrNo
    print("Do you want another card?")
    answer = getYesOrNo()
    if answer == 'yes':
        return True
    else:
        return False

def getDealerCard(dealer, deck):
    """deals another card to the dealer and displays the new hand and its score"""
    card = deck.deal()
    dealer.addCard(card)
    print(f"The {card} was dealt to the dealer.")

def main():
    """blackjack"""
    playAgain = True  # game loop variable
    playerWins = 0
    dealerWins = 0

    print(f"Let's play BlackJack!")
    print()

    while playAgain:
        # create new deck and prepare player hands
        deck = Deck()
        deck.shuffle()

        # prepare player and dealer hands with starting cards
        player = dealHand(deck)
        dealer = dealHand(deck)

        # show player's hand and score
        displayHandAndScore(player, "Player")
        print()

        # show dealer's second card
        print(f"Dealer's second card: {dealer[1]}")
        print()

        # ask player if they want another card
        while getAnotherCard():
            player.addCard(deck.deal())
            displayHandAndScore(player, "Player")
            print()

        if player.isBusted():
            print("You busted. The dealer wins!")
            dealerWins += 1
        else:
            displayHandAndScore(dealer, "Dealer")
            print()
            while dealer.score() < 17:
                getDealerCard(dealer, deck)
                displayHandAndScore(dealer, "Dealer")
                print()
            if dealer.isBusted():
                print("The dealer busted. You win!")
                playerWins += 1
            elif player.score() > dealer.score():
                print("You win.")
                playerWins += 1
            elif dealer.score() > player.score():
                print("The dealer wins.")
                dealerWins += 1
            else:
                print("It's a tie.")
            print()

        playAgain = game.playAgain()

    print(f"Total player wins: {playerWins}")
    print(f"Total dealer wins: {dealerWins}")
    print()
    print("Thanks for playing!")


if __name__ == '__main__':
    main()
