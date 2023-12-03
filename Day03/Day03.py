import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(3)

def checkBoundary(r, c):
  for dr in [-1, 0, 1]:
    for dc in [-1, 0, 1]:
      rr = r + dr
      cc = c + dc
      if 0<=rr<R and 0<=cc<C:
        symbol = _input[rr][cc]
        if symbol == "*":
          gears.add((rr,cc))
        if not symbol.isdigit() and symbol != ".":
          return True
  return False

p1_ans = 0
p2_ans = -0
R = len(_input)
C = len(_input[0])
good = []
bad = []
gears = set()
numbers = defaultdict(list)
for row in range(R):
  currentNum = 0
  adjacent = False
  for col in range(C):
    if _input[row][col].isdigit():
      current = _input[row][col]
      currentNum = currentNum * 10 + int(current)
      adjacent = adjacent or checkBoundary(row, col) 
    elif currentNum > 0:
      # have a number, but found a '.' or symbol.
      for gear in gears:
        numbers[gear].append(currentNum)
      if adjacent:
        #print(f"adding {currentNum}")
        good.append(currentNum)
        p1_ans += currentNum
      else:
        bad.append(currentNum)
      currentNum = 0
      adjacent = False
      gears = set()
  
  if currentNum > 0 and adjacent:
    for gear in gears:
      numbers[gear].append(currentNum)
    p1_ans += currentNum
    currentNum = 0
    adjacent = False
    gears = set()

for k,v in numbers.items():
  if len(v) == 2:
    p2_ans += (v[0] * v[1])
print(p1_ans)
print(p2_ans)
#print(good)
#print(bad)