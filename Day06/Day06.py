import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(6)

def doRace(times, distances):
  race = 0
  winners = defaultdict(list)

  while race < len(times):
    time = times[race]
    distanceToBeat = distances[race]
    for holdButton in range(time):
      remainingTime = time - holdButton
      distance = holdButton * remainingTime
      
      if distance > distanceToBeat:
        winners[time].append(distance)
    race += 1

  ans = 1
  for k, v in winners.items():
    ans *= len(v)
  print(ans)

t = [int(x) for x in _input[0].split(':')[1].strip().split()]
d = [int(x) for x in _input[1].split(':')[1].strip().split()]

doRace(t, d)

t = [int("".join(_input[0].split(":")[1].strip().split()))]
d = [int("".join(_input[1].split(":")[1].strip().split()))]

doRace(t, d)
