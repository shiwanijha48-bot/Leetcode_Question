class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}  # store frequency of chars in s
        for i in s:  # loop through string s
            if i not in count:
                count[i] = 1  # first occurrence
            else:
                count[i] += 1  # increment count
        for j in t:    # loop through string t
            if j not in count or count[j] == 0:
                return j   # extra char found
            else:
                count[j] -= 1   # reduce count
        return ""      # fallback(should not happen)
        
