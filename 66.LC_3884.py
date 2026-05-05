class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)  # length of string
        for i in range(0, n):  # loop from start to end
            if s[i] == s[n-i-1]:  # char from left and right
                return i  # if equal, return 1st smallest indez
        return -1  # if not such index found 
