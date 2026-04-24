class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}  # dict to store freq
        for i in s:   #  count each character
            if i not in count:   
                count[i] = 1
            else:
                count[i] += 1
        r = ""   # final answer string
        for ch in sorted(count, key = count.get, reverse = True): # sort keys based on the highest first
            r += ch*count[ch]  # add character multiple times
        return r  

#  TC -> O(n + k log k)
#  SC -> O(n)
