#!/usr/bin/env python
import random
# Bin filled with balls 1, 2, ..., n
# Pick balls uniformly at random without replacement
# 3, 1, 4, 5, 2 (n=5)

# rand(n) returns 0 to n-1

class BallPicker:
    def __init__(self, n):
        # use array for balls
        # create array with values in slot
        # a = [ 1, 2, 3, 4, 5]
        self.arr = [] * n
        self.orign = n
        self.picked = 0
        self.reset()
        print("doing bp init")
        
    def pick_ball(self):
        # r = rand(n)
        # select item at r , return
        # pop off end off array, copy value into a[r]
        if 0 == len(self.arr):
            return -1
        r = random.randrange(self.orign - self.picked ) # r in index 
        print(f"picked r {r} from arr {self.arr} picked {self.picked}")
        val = self.arr[r]
        popval = self.arr.pop()
        
        # move last element into the slot chosen unless it's the last one. In that case do nothing
        if r < self.orign - self.picked - 1:
          self.arr[r] = popval
        self.picked += 1
        # pop: 5
        # copy 5 into slot we just picked from a[2] -> a[1, 2, 5, 4]
        return val # a[2]
        
    def reset(self):
        self.picked = 0
        self.arr = [  i + 1 for i in range(self.orign) ] # 5 => [ 1, 2, 3, 4, 5] 
     
    def get_num_balls_picked(self):
        return self.picked
    
class BallPicker2:
    def __init__(self, n):
        self.picked = 0
        self.orign = n
        self.picked_balls = set()
        
    def pick_ball(self):
        # assume n much larger k
        r = random.randrange(self.orign - len(self.picked_balls))
        if r in self.picked_balls:
            return self.pick_ball()
        else:
            self.picked_balls.add(r)
            return r
        pass # should never get here
    
def main():
    print("doing main")
    n = 100000000 # 
    n = 10
    # pick 5 balls
    #r = random.randint(n - picked)
    # add val to set()
    # each iteration: get another
    # if val in set, repick
    
    k = 10
    bp = BallPicker(n)
    for i in range(k):
        print(bp.pick_ball())

if __name__ == '__main__':
    main()

