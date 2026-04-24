class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:  # base cases 
            return n  # for 1 -> 1, for 2 -> 2
        x = 1 # step 1
        y = 2 # step 2
        for _ in range(3, n+ 1):
            x, y = y, x + y  # logic fibonacci, new x = old y, new y = old x+ old y => f(n) = f(n-1) + f(n-2)
        return y

#  TC -> O(N)
#  SC -> O(1)
