class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n # store res of each index
        for i in range(0, n):
            count = 0 # even or odd count
            if nums[i] % 2 == 0: # if num is even
                for k in range(i + 1, n):
                    if nums[k] % 2 != 0: # store odd 
                        count += 1 # count them
            else:
                for k in range(i + 1, n):
                    if nums[k] % 2 == 0:
                        count += 1
            res[i] = count
        return res
                    
