# Project Euler Problem 54
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand	 	Player 1	 	    Player 2	 	    Winner
#   1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
#           Pair of Fives       Pair of Eights

#   2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
#           Highest card Ace    Highest card Queen

#   3	 	2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
#           Three Aces          Flush with Diamonds

#   4	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
#           Pair of Queens      Pair of Queens
#           Highest card Nine   Highest card Seven

#   5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
#           Full House          Full House
#           With Three Fours    with Three Threes

# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

from collections import Counter
import math

card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def SplitSuits(l):
    cards = []
    suits = []
    for i in l:
        cards.append(card_values[i[0]])
        suits.append(i[1])
    hand = [cards, suits]
    return hand

def CheckFlush(l):
    if len(set(l[1])) == 1:
        v = l[0]
        v.sort()
        return v[-1]
    return 0

def CheckStraight(l):
    if len(set(l[0])) == 5:
        v = l[0]
        v.sort()
        for i in range(len(v)-1):
            if v[i] + 1 != v[i + 1]:
                return 0
        return v[-1]
    return 0

def CheckFull(l):
    if CheckThree(l) != 0 and CheckPairs(l)[0] != 0:
        return CheckThree(l)
    return 0

def CheckStraightFlush(l):
    if CheckStraight(l) != 0 and CheckFlush(l) != 0:
        return CheckStraight(l)
    return 0

def CheckFour(l):
    if len(set(l[0])) == 2:
        v = l[0]
        v.sort()
        a = Counter(v)
        if 4 in a.values():
            card = a.most_common(1)[0][0]
            return card
    return 0

def CheckThree(l):
    if len(set(l[0])) >= 2:
        v = l[0]
        v.sort()
        a = Counter(v)
        if 3 in a.values():
            card = a.most_common(1)[0][0]
            return card
    return 0

def CheckPairs(l):
    v = l[0]
    v.sort()
    a = Counter(v)
    if (a.most_common(2)[0][1] == 2) and (a.most_common(2)[1][1] == 2):
        b_pair = a.most_common(2)[1][0]
        s_pair = a.most_common(2)[0][0]
        return s_pair, b_pair
    if a.most_common(1)[0][1] == 2:
        pair = a.most_common(1)[0][0]
        return pair, 0
    return 0, 0

def CalcScore(l):
    score = 0
    v = l[0]
    v.sort()
    for i in range(len(v)):                     # Calculate single values of cards into 10^0 to 10^4 before considering combinations
        score = score + v[i] * (10 ** i)
    p = CheckPairs(l)
    for i in range(len(p)):                     # Add pairs values to 10^5 and 10^6 positions
        score = score + p[i] * (10 ** (i + 5))
    score = score + (CheckThree(l) * (10 ** 7)) # Add three of a kind value to 10^7 position
    score = score + (CheckStraight(l) * (10 ** 8)) # Add straight top card value to 10^8 position
    score = score + (CheckFlush(l) * (10 ** 9)) # Add flush top card value to 10^9 position
    score = score + (CheckFull(l) * (10 ** 10)) # Add full house three card value to 10^10 position
    score = score + (CheckFour(l) * (10 ** 11)) # Add four of a kind card value to 10^11 position
    score = score + (CheckStraightFlush(l) * (10 ** 12)) # Add top of straight flush card value to 10^12 position
    
    return score

f = open("p054_poker.txt", "r")
content = f.read()
content_list = content.splitlines()
f.close()

games = []

for i in content_list:
    p1 = []
    p2 = []
    for j in i.split(' ')[:5]:
        p1.append(j)
    for j in i.split(' ')[5:]:
        p2.append(j)
    hands = [p1, p2]
    games.append(hands)

wins = 0

for i in games:
    p1 = SplitSuits(i[0])
    p2 = SplitSuits(i[1])
    if CalcScore(p1) > CalcScore(p2):
        wins = wins + 1

print(wins)
