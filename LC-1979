class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ans = 1
        a = min(nums)
        b = max(nums)
        for i in range(1, min(a,b)+1):
            if a%i == 0 and b%i == 0:
                ans = i
        return ans
#  TC -> O(n + min(a,b))
#  SC -> O(1)
