# ------------------- TLE -----------------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        for i in range(0, n):
            num = nums[i]
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1 
            max_count = max(max_count, count)
        return max_count
# -------------------------------------------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort() # sorting so consecutive nums are next to each other and it takes nlogn
        count = 0  # current consecutive sequence length
        last_smaller = float('-inf')  # to keep track of prev num
        longest = 0   # output = longest sequence found
        # for i in range(0,n):
        #     num = nums[i]
        for num in nums:
            if num-1 == last_smaller: # check if curr is consecutive
                count += 1
                last_smaller = num
            elif num != last_smaller:  # skip duplicates
                count = 1
                last_smaller = num
            longest = max(longest, count) # update the answer
        return longest
# ----------------------------------------------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set()
        for i in range(0, n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest
