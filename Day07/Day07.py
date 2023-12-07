import sys
import math
from enum import Enum
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(7)

joker = True
ranks = { "A": 14, "K": 13, "Q": 12, "J": 1 if joker else 11, "T": 10, "9": 9, "8" : 8,"7" : 7,"6" : 6,"5" : 5,"4" : 4,"3" : 3,"2" : 2, }

class Hand(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

def determineHand(hand, containsJokers = False):
  counts = defaultdict(int)
  jokers = 0
  for card in hand:
    if containsJokers and card != 'J':
      counts[card] = hand.count(card)
    elif containsJokers and card == 'J':
      counts[card] = hand.count(card)
      jokers += 1
    else:
      counts[card] = hand.count(card)
  
  hand = [ranks[card] for card in hand]
  
  r = [(key, ranks[key], counts[key]) for key in counts.keys()] 
  bestHand = sorted(r, key=lambda item: (item[2], item[1]), reverse=True)[0]
  
  counts[bestHand[0]] += jokers

  if 5 in counts.values():
    return (Hand.FIVE_OF_A_KIND.value, hand)
  elif 4 in counts.values():
    return (Hand.FOUR_OF_A_KIND.value, hand)
  elif sorted(counts.values()) == [2, 3]:
    return (Hand.FULL_HOUSE.value, hand)
  elif 3 in counts.values():
    return (Hand.THREE_OF_A_KIND.value, hand)
  elif sorted(counts.values()) == [1, 2, 2]:
    return (Hand.TWO_PAIR.value, hand)
  elif sorted(counts.values()) == [1, 1, 1, 2]:
    return (Hand.ONE_PAIR.value, hand)
  else:
    return (Hand.HIGH_CARD.value, hand)

hands = []
for line in _input:
  hand, bet = line.split()
  strength, computedHand = determineHand(hand, joker)
  hands.append((hand, bet, strength, computedHand))

hands = sorted(hands, key=lambda item: (item[2], item[3]))

ans = 0
for i, (hand, bet, _, _) in enumerate(hands):
  print(i, hand, bet)
  ans += (int(bet) * (i+1))

print(ans)
