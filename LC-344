# 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1
        while first < last:  # runs until both ptrs meet
            s[first], s[last] = s[last], s[first]  # swap karna
            first += 1
            last -= 1 
#  TC -> O(N)
#  SC -> 0(1)
