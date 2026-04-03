class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # last unique ele, initialy first ele
        j = i + 1  # next ele to check
        while j < len(nums):   # until nums is empty, j moves
            if nums[j] != nums[i]:   # no duplicate ele
                i += 1 # new next unique positn
                nums[j] , nums[i] = nums[i], nums[j] # swap new unique ele to correct positn
            j += 1 # j to next ele
        return i + 1  # i is index of last unique ele, i+1 = total unique ele
        
#  TC -> O(n)
# SC -> O(1)  
