class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}   # counting the freq of each elemnts
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for j in range(0, len(s)): # checking the str ka har ek lements
            if count[s[j]] == 1:   # checking count me key jiski value s[i] ho agar uska value= 1 h to return it
                return j
        return -1   # else return -1


#  TC -> O(N)
#  SC -> O(N) count le rha h worst me saare elemetsn
