import sys
import math
from itertools import pairwise
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(9)

def calculateNext(history):
  history = list(reversed(history))

  for i, v in enumerate(history):
    if i + 1 < len(history):
      for j in [-1, 0]:
        previousHistoryVal = history[i+1][j]
        currentHistoryVal = history[i][j]
        prediction = (previousHistoryVal + currentHistoryVal) if j == -1 else previousHistoryVal - currentHistoryVal
        history[i+1].append(prediction) if j == -1 else history[i+1].insert(0, prediction)
  
  return history

def calculateSteps(line):
  history = []
  line = [int(x) for x in line.split()]
  history.append(line)
  while True:
    nextStep = []
    for first, second in list(pairwise(line)):
      step = int(second) - int(first)
      nextStep.append(step)

    history.append(nextStep)
    if all([s == 0 for s in nextStep]):
      break
    line = nextStep
  return history

p1_ans = 0
p2_ans = 0
for line in _input:
  history = calculateSteps(line)
  history = calculateNext(history)
  p1_ans += history[-1][-1]
  p2_ans +=  history[-1][0]
print(p1_ans)
print(p2_ans)