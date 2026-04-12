class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        for i in range(n):
            if haystack[i : i + m] == needle:
                return i
        return -1
===========================================================================
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(0,n-m + 1):
            for j in range(0, m):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1 
