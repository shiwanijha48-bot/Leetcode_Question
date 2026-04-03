class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""   # empty str
        for i in s:  # chcking each ch in str s
            if i.isalnum(): # letters + num only allowed
                r = r + i  # then add in str r
        r = r.lower()   # lowercase to compare easily
#  Two pointer Approach
        f = 0    # first
        l = len(r) -1   # last
        while l > f:   # until both becomes coincide
            if r[f] != r[l]:   # not equal
                return False
            f += 1   # f moves aage
            l -= 1   # l moves piche
        return True

#  TC -> O(n)
#  SC -> O(n)  # new str r banaya
