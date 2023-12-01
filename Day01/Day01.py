import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(1)


nums = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven":7, "eight": 8, "nine": 9 }


ans = 0

for line in _input:
  digits = []
  for i, c in enumerate(line):
    if c.isdigit():
      digits.append(c)
    for k, v in nums.items():
        if line[i:].startswith(k):
           digits.append(str(v))

  ans += int(digits[0] + digits[-1])

print(ans)