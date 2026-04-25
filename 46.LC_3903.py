class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)   # no of elemnts
        for i in range(0, n):  # every index 
            maxleft = float('-inf') #max of left part(0->i)
            for j in range(0, i+1): 
                maxleft = max(maxleft, nums[j]) # update max on lft side
            minright = float('inf') # store min of right(i -> n-1)
            for j in range(i, n): 
                minright = min(minright, nums[j])  # update min on right
            if maxleft - minright <= k:  # checking the conditon
                return i     # return first index 
        return -1    # no valid index found
