import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(4)

ans = 0
scratchers = defaultdict(int)
for line in _input:
  card, rest = line.split(":")
  cardNum = int(card.split()[1])
  winningNumbers, myNumbers = rest.strip().split('|')
  winningNumbers = winningNumbers.strip()
  myNumbers = myNumbers.strip()
  
  winningSet = set(winningNumbers.split())
  myNumbersSet = set(myNumbers.split())

  scratchers[cardNum] += 1

  overlap = myNumbersSet.intersection(winningSet)
  exponent = len(overlap) - 1

  for i in range(1, len(overlap) + 1):
    scratchers[cardNum+i] += (1 * scratchers[cardNum]) 

  if len(overlap) == 0:
    continue
  
  ans += int((2**exponent))

print(ans)
print(sum([v for k, v in scratchers.items()]))