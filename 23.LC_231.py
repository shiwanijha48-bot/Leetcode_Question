class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:  #  poweer of 2 should be always positive
            return False    # power cant be zero or negative 
        while n % 2 == 0:    # loop runs while n is divisible by 2
            n = n//2      # divide n by 2, reducing num step by step
        if n == 1:      # loop ends. n = 1 it means power of 2 is valid
            return True
        else:
            return False
#  Tc -> O(log n)
#  Sc ->  O(1)
