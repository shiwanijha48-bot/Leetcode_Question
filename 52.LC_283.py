class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: # edge case: only one ele, then no need of 2 ptr approach
            return 
        i = 0  # ptr 1 at start
        while i < len(nums): # more than one elemnts
            if nums[i] == 0:  # if ele is 0, then break
                break
            i += 1 # move i if not zero
        if i == len(nums): # if it reached to end, return
            return 
        j = i + 1 # 2nd ptr, after i
        while j < len(nums):  # it has more ele 
            if nums[j] != 0:  # if found nonzero bring it to position i
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1   # move i to next zero ptr
            j += 1  # always move j forward
