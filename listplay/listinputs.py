#!/usr/bin/env python

if __name__ == '__main__':
  num_commands = int(input())
  commands = [ str(input()).split()  for c in range(num_commands)] 

  result = []
  for c in commands:
    func = c[0]
    args = c[1:]

    if func == "insert":
      i = int(args[0])
      e = int(args[1])
      if len(result) < i:
        padding = [0] * (i - len(result) + 1)
        print(f"doing padding {padding}")
        result = result + padding
        result[i] = e
      else:
        result = result[:i] + [e] + result[i:]
    elif func == "print":
      print(result)
    elif func == "remove":
      i = result.index(int(args[0]))
      del result[i]
    elif func == "append":
      result.append( int(args[0]) )
    elif func == "sort":
      result.sort()
    elif func == "pop":
      result.pop()
    elif func == "reverse":
      result.reverse() # reverse in place
