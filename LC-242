1-------------------------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}  # freq of str s elements
        count2 = {}  # freq of str t elemsnts
#  optimization 
        if len(s) != len(t):
            return False
        for i in s:
            if i not in count1:  
                count1[i] = 1
            else:
                count1[i] += 1
        for j in t:
            if j not in count2:
                count2[j] = 1
            else:
                count2[j] += 1
        if count1 == count2:
            return True
        else:
            return False
#  TC -> O(n)
#  SC -> O(n)


2------------------------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
