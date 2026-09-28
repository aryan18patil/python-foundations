"""
Poker is a card game that uses a standard deck of cards. There are 52 cards in a standard deck - 4 suits of 13 cards. The suits are: Spades, Clubs, Hearts and Diamonds. The 13 cards
consist of the Ace ('A'), cards 2 to 10, and the face cards, the Jack ('J'), Queen ('Q') and King ('K'). When we talk about a card, we need to specify its value and its suit. We can use a
tuple to do this. For example, the tuple ('A', 'Spades') represents the card the Ace of Spades. The tuple ('9', 'Hearts') represents the card the 9 of Hearts.

In Poker, a player gets dealt 5 cards. This is referred to as a 'Poker hand'. We will represent a Poker hand using a list of 5 tuples, where each tuple represents a card as discussed
previously. Poker hands are ranked based on the cards they contain. One such rank is called the 'Flush'. With a 'Flush', all cards in the hand have the same suit.

Given this information, complete the is_hand_a_flush() function that takes a list of 5 tuples as parameter called poker_hand. The function returns True if the poker hand is a Flush and
False otherwise.
"""

def is_hand_a_flush(poker_hand):
    suit = poker_hand[0][1]
    flush = True
    i = 1
    
    while (i < len(poker_hand)) and (flush):
        if poker_hand[i][1] != suit:
            flush = False
            
        i += 1
        
    return flush

poker_hand = [('A', 'Spades'), ('3', 'Spades'), ('J', 'Spades'),
              ('6', 'Spades'), ('9', 'Spades')]
if is_hand_a_flush(poker_hand):
    print("Your poker hand is a Flush!")
else:
    print("Your poker hand is not a Flush!")

poker_hand = [('8', 'Hearts'), ('2', 'Diamonds'), ('A', 'Spades'),
              ('7', 'Clubs'), ('Q', 'Hearts')]
if is_hand_a_flush(poker_hand):
    print("Your poker hand is a Flush!")
else:
    print("Your poker hand is not a Flush!")

poker_hand = [('Q', 'Hearts'), ('J', 'Hearts'), ('K', 'Hearts'),
              ('9', 'Hearts'), ('4', 'Diamonds')]
if is_hand_a_flush(poker_hand):
    print("Your poker hand is a Flush!")
else:
    print("Your poker hand is not a Flush!")
