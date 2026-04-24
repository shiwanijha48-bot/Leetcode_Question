class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)   # no of elemnt
        total = n * (n+1) // 2  # sum off numbers from 0 to n      
        sumArr = 0   
        for i in nums:  # all elemnts of arr
            sumArr += i   # add all elemnt of arr
        return total - sumArr   # missing number = total - sumarr
