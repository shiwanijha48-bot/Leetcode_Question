class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []  # list of nums valid
        for i in range(0, n):
            left = True  # valid then true
            right = True
            for j in range(0, i):  # check left side
                if nums[j] >= nums[i]:  # if left side has num bigger than curr num
                    left = False  # invalid, so make it false
                    break  # no need to check further
            for j in range(i+1, n):  # check right side similarly
                if nums[j] >= nums[i]:
                    right = False
                    break
            if left == True or right == True:  # if any side is valid
                ans.append(nums[i]) # add the num in the ans list
        return ans

#  TC -> O(n^2)  worst case
