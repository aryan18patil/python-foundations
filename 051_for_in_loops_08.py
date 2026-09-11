"""
Blackjack is a card game sometimes called Twenty-One. The object of Blackjack is to have a hand of cards whose score is 21, or as close to this as possible. A player whose hand exceeds a
score of 21 is said to have bust and loses. A hand in Blackjack is scored as follows:

Cards 2 to 10 are given their card value as points (i.e. 2 to 10 points).
Face cards, the Jack, Queen and King, are all worth 10 points.
The Ace card is worth 11 points, or 1 point if doing so prevents the player from going bust. For example, if a player's hand has three Aces and a 6, one of the Aces will be worth 11
points, while the other two will be worth 1 point, making the score for the hand 19 (11 + 1 + 1 + 6). If all three Aces are worth 11, then the score for the hand would be 39 (11 + 11 + 11
+ 6) and the player would be bust. Similarly, if two of the Aces are worth 11 points, then the score of the hand would be 29 (11 + 11 + 1 + 6) and the player would also be bust.


Code the blackjack_hand_score() function that takes a single list of strings (hand) as parameter called hand and calculates its score. The cards in a hand are represented as strings:

Cards 2 to 10 are represented as "2", "3", ..., "10".
Face cards, the Jack, Queen and King, are represented as "J", "Q" and "K".
The Ace card is represented as "A".
"""

def blackjack_hand_score(hand):
    
    score = 0
    ace_count = 0
    
    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
            
        elif card in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            score += int(card)
            
        elif card == "A":
            ace_count += 1
            score += 11
            
    while (score > 21) and (ace_count > 0):
        score -= 10
        ace_count -= 1
        
    return score
