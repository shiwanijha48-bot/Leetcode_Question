class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # valid elemnt ptr
        for j in range(0, len(nums)): # entire loop
            if nums[j] != val:  # only ele not equal to val
                nums[i] = nums[j] # placing valid ele at front
                i += 1 # moving forward ptr in res arr
        return i  # length of updated arr
    
#  TC -> O(N)
#  SC -> O(1)
