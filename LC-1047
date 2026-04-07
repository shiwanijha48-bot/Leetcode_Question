class Solution:
    def removeDuplicates(self, s: str) -> str:
        r = []   # empty list
        for i in s:   # ch in str s
            if r and r[-1] == i:  # r: lst not empty, r[-1]= last element is equal to the i
                r.pop() # same ele, then pop
            else:
                r.append(i)  # otherwoise add
        return "".join(r) # coverts list to string, and join all characters

        #  TC -> o(n)
        #  SC -> o(1)
