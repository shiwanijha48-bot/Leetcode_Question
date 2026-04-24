class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2) # cponverted into int
        b = int(b,2)
        return bin(a + b)[2:] # copnverted into bin after adding int nums, then removed 0b by [2:]
#  TC -> O(m+n)
#  SC -> O(m+n)
