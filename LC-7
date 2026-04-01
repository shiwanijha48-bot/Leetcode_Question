# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 # positive for x > 0
        if x < 0: # negative x
            sign = -1   # sign negative 
            x = (-1) * x  # make num positive to calculate rev, then multioply by sign
    
        while x > 0:
            ld = x % 10
            rev = rev * 10 + ld
            x = x//10
        rev = rev * sign  # rev multiply by sign according to +ve or -ve

        if rev < -2**31 or rev > 2**31 -1:   # out of constraints the return 0 karna h
            return 0
        return rev
#  TC -> O(N)
#  SC -> O(1)
