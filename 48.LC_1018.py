class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [] # store the true/false for each possible outcome of nums
        s = ""  
        for bits in nums:  # traversing each bits
            s = s + str(bits)  # binary string 
            num = int(s,2)   # convert to decimal
            res.append(num % 5 == 0) # check divisibility by 5
        return res
 
