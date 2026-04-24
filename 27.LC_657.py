class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0   # robot is at origin (0,0)
        for i in moves:  # loop for each char in str,UDLR
            if i == 'U': # move up
                y += 1  # step 1 up, inc y
            elif i == 'D':  # down 
                y -= 1   # step 1 down, dec y
            elif i == 'L':  # left
                x -= 1   # step 1 left, inc x
            elif i == 'R':   # move right
                x += 1   # step 1 right, dec x
        if x == 0 and y == 0:  # robot if back to origin(0,0)
            return True
        else:
            return False
#  TC -> O(N)
#  SC -> O(1)
