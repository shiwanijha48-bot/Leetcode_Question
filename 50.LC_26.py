class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)  # length of input list
        freq_map = {}   # dict to store unique elements
        for i in range(0, n):   # loop through each elemnt
            freq_map[nums[i]] = 0   # add ele as key,removes duplicates automatically
        j = 0  # ptr to place unique ele in nums
        for k in freq_map: # iterate over unique keys
            nums[j] = k  # place unique ele at index j
            j += 1   # move ptr forward
        return j   # cnt of unique ele
