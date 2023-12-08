import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(8)

instructions = _input[0]

routes = defaultdict(list)
for line in _input[2:]:
  source, destinations = line.split(" = ")
  left, right =  destinations.replace('(', '').replace(")", "").split(', ')
  routes[source] = [left, right]

def dostep(current):
  instructionIndex = 0
  steps = 0
  while True:
    currentInstruction = instructions[instructionIndex]
    if currentInstruction == 'L':
      current = routes[current][0]
    else:
      current = routes[current][1]
    
    if current.endswith('Z'):
      steps += 1
      break
    steps += 1
    instructionIndex = (instructionIndex + 1) % len(instructions)
  
  #print(steps)
  return steps

def lcm(*integers):
  a = integers[0]
  for b in integers[1:]:
      a = (a * b) // math.gcd (a, b)
  return a

print(dostep('AAA'))

elements = [route for route, _ in routes.items() if route.endswith('A')]
paths = [dostep(start) for start in elements]
print(lcm(*paths))