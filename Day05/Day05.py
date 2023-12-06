import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(5)

def findConversionValue(sourceNum, values):
  for map in values:
    
    destinationRangeStart = int(map[0])
    sourceRangeStart = int(map[1])
    rangeLength = int(map[2])
    
    if sourceRangeStart <= int(sourceNum) and (sourceRangeStart + rangeLength) >= int(sourceNum):
      return destinationRangeStart + (sourceNum - sourceRangeStart)
  #handle case where it doesnt exist in the map
  return sourceNum

seeds = [int(x) for x in _input[0].split(":")[1].strip().split()]

maps = []

for i, line in enumerate(_input[1:]):
  if "map" in line:
    ranges = []
    for j, val in enumerate(_input[i+1:]):
      if "map" in val:
        continue
      if len(val) == 0:
        break
      ranges.append([int(x) for x in val.split()])
    maps.append(ranges)

locations = []
for seed in seeds:
  #print(f"doing seed {seed}")
  nextLookup = seed
  for i, map in enumerate(maps):
    nextLookup = findConversionValue(nextLookup, map)
  
  locations.append(nextLookup)
  #print(f"seed {seed}, location {nextLookup}")
  
print(min(locations))


# this naive brute force aint gonna work
locations = []
for i, seed in enumerate(range(0, len(seeds) ,2)):
  currentSeed = seeds[seed]
  rangeOfSeeds = seeds[seed+1]
  print(f"doing seeds {currentSeed}-{currentSeed+rangeOfSeeds-1}")

  for j, newSeed in enumerate(range(currentSeed, currentSeed + rangeOfSeeds, 1)):
    #print(f"doing seed {newSeed}")
    nextLookup = newSeed
    for i, map in enumerate(maps):
      nextLookup = findConversionValue(nextLookup, map)
    
    locations.append(nextLookup)
    #print(f"seed {seed}, location {nextLookup}")
  
print(min(locations))