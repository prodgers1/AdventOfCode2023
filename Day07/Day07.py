import sys
import math
from enum import Enum
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(7)

ranks = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8" : 8,"7" : 7,"6" : 6,"5" : 5,"4" : 4,"3" : 3,"2" : 2, }

class Hand(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

def determineHand(hand):
  counts = defaultdict(int)
  for card in hand:
    counts[card] = hand.count(card)
  
  for card in hand:
    hand = hand.replace(card, str(ranks[card]))

  # 5 of a kind
  if 5 in counts.values():
    return (Hand.FIVE_OF_A_KIND.value, hand)
  elif 4 in counts.values():
    return (Hand.FOUR_OF_A_KIND.value, hand)
  elif sorted(counts.values()) == [2, 3]: #full house?
    return (Hand.FULL_HOUSE.value, hand)
  elif 3 in counts.values() : # three of a kind
    return (Hand.THREE_OF_A_KIND.value, hand)
  elif sorted(counts.values()) == [1, 2, 2]: # two pair
    return (Hand.TWO_PAIR.value, hand)
  elif sorted(counts.values()) == [1, 1, 1, 2]: #one pair
    return (Hand.ONE_PAIR.value, hand)
  else: #high card
    return (Hand.HIGH_CARD.value, hand)

hands = []
for line in _input:
  hand, bet = line.split()
  hands.append((hand, bet))

hands = sorted(hands, key=lambda item: determineHand(item[0]))

ans = 0
for i, (hand, bet) in enumerate(hands):
  print(i, hand, bet)
  ans += (int(bet) * (i+1))

print(ans)