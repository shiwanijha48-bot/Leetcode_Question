class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')  #inf to calc min dist
        for i in range(0, len(nums)): 
            if nums[i] == target: # find index of eql ele of nums with target
                distance = abs(i-start)  # distance. absolute btw i and start
                ans = min(ans, distance)  # min dist possible
        return ans

#  TC -> O(n)
#  SC -> O(1)
