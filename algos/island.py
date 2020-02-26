#!/usr/bin/env python
from pprint import pprint
"""
Given a map represented as a two-dimensional array of 1’s and 0’s, where 1’s are land and 0’s are water, write a method that determines how many separate islands are contained in the map.

An example:

```
0 0 1 0 0 0
0 0 1 1 0 0
0 0 0 1 0 0 ==> 3 islands
1 0 0 0 1 0
0 0 0 0 1 0
```
explanation:

```
0 0 A 0 0 0
0 0 A A 0 0
0 0 0 A 0 0 ==> island A, island B, and island C (A isn't connected to C)
B 0 0 0 C 0
0 0 0 0 C 0
```
"""

seen = set()
def findIsland(arr):
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == 0:
                continue
            elif (x,y) in seen:
                continue
            elif arr[x][y] == 1:
                # discover entire island connectioned to (x,y)
                print("marking island at %d %d" % ( x,y))
                discoverIsland(arr, x, y)
                result += 1
    return result

def discoverIsland(arr, x, y):
    print("discovering %d %d" % (x,y))
    if (x,y) in seen:
        return
    seen.add( (x,y) )
    if x >= len(arr):
        return
    if y >= len(arr[0]):
        return
    if x > 0 and arr[x-1][y] == 1:
        discoverIsland(arr, x-1, y)
        seen.add((x-1,y))
    if x < len(arr) - 1 and arr[x+1][y] == 1:
        discoverIsland(arr, x+1, y)
        seen.add((x+1,y))
    if y < len(arr[0]) -1  and arr[x][y+1] == 1:
        discoverIsland(arr, x, y+1)
        seen.add((x,y+1))
    if y > 0 and arr[x][y-1] == 1:
        discoverIsland(arr, x, y-1)
        seen.add((x,y-1))

def main():
  a = [ [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0] ]
  pprint(a)
  c = findIsland(a)
  print("found %d islands " % c)

if __name__ == '__main__':
  main()
