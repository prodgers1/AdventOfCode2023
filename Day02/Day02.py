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
    if ',' in round:
      colors = round.split(', ')
      for color in colors:
        num, c = color.split(' ')
        roundDict[c] = int(num)
    else:
      num, c = round.split(' ')
      roundDict[c] = int(num)

    roundsList.append(roundDict)

  return gameNum, roundsList
    
p1= True
ans = 0
possibleRounds = []
for l in _input:
  gameNum, rounds = parse(l)
  if p1:
    impossible = False
    for round in rounds:
      for k, v in round.items():
        if (k == "blue" and v > MAX_BLUE) or (k == "red" and v > MAX_RED) or (k == "green" and v > MAX_GREEN):
          impossible = True
    
    if not impossible:
      possibleRounds.append(int(gameNum))
  else:
    MINS = defaultdict()
    for round in rounds:
      for i, color in enumerate(["red", "green", "blue"]):
        if color in round:
          if color not in MINS:
            MINS[color] = 0
          MINS[color] = max(MINS[color], round[color])
    
    power = 1
    for k, v in MINS.items():
      power *= v
    ans += power
    


if p1:
  #print(possibleRounds)
  print(sum(possibleRounds))
else:
  print(ans)