class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)  # smallest num
        maxi = max(nums)  # greatest num
        res = []   # storing missing nums
        for i in range(mini, maxi + 1):
            if i not in nums:   # if  num not in arr
                res.append(i)  # add to res
        return res
