class Solution:
    def romanToInt(self, s: str) -> int:
        values = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D': 500, 'M' : 1000}  # dict to store roman symbol and their vals
        total = 0  # variable to store the final ans
        n = len(s)
        for i in range(0, n):  # each char of str (0 to n-1)
            if i < n-1 and values[s[i]] < values[s[i+1]]: # 2 checkpoints-> i dont go out of bounds. curr val is maller than next val. IV= 1<5:subtract total = 0-1
                total -= values[s[i]] # subtract curr val from total
            else:
                total += values[s[i]]  # add the values VI= 5>1: add total = 5+1
        return total

#  TC -> O(n)
#  SC -> O(1)
