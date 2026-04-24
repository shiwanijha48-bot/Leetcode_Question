class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0   # start
        r = len(nums) - 1  # end
        while l <= r:   # valid range exists
            mid = (l + r)//2   # midd index
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # target is bigger
                l = mid + 1 # search in right half
            else:    # target is smaller
                r = mid - 1   # serach in left half
        return l  # position where target inserteed

#  Binary Search
#  TC -> O(log n)
