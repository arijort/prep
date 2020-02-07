#!/usr/bin/env python

from collections import Counter

def main():
  print("make some arrays")
  # preprocess array to contain at most 3 of any nonunique numbers
  arr = [0, 0, 1, 2, 3, 4, 4, 4, 4, 5]
  
  d = dict()
  for s in arr:
    if s not in d:
      d[s] = 1
    elif d[s] == 3: 
      continue
    else:
      d[s] += 1
  print("from array %s result is %s" % (str(arr), str(d)))
  c = Counter(d)
  print("with counter %s " % sorted(c.elements()))

if __name__ == '__main__':
  main()
