import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(2)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def parse(line):
  gameNum, rest = line.split(': ')
  gameNum = gameNum.split(' ')[1]
  rounds = rest.split('; ')
  roundsList = []

  for round in rounds:
    roundDict = defaultdict()
    colors = round.split(', ')
    for color in colors:
      num, c = color.split(' ')
      roundDict[c] = int(num)

    roundsList.append(roundDict)

  return gameNum, roundsList
    
ans = 0
possibleRounds = []
for l in _input:
  gameNum, rounds = parse(l)
  MINS = defaultdict(int)
  impossible = False
  for round in rounds:
    for k, v in round.items():
      if (k == "blue" and v > MAX_BLUE) or (k == "red" and v > MAX_RED) or (k == "green" and v > MAX_GREEN):
        impossible = True
      MINS[k] = max(MINS[k], round[k])
  
  if not impossible:
    possibleRounds.append(int(gameNum))
  power = 1
  for k, v in MINS.items():
    power *= v
  ans += power
    

#print(possibleRounds)
print(sum(possibleRounds))
print(ans)