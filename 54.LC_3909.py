class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        peak = 0
        for i in range(1,n):
            if nums[i] > nums[peak]:
                peak = i
        asc = 0
        for i in range(0, peak +1):
            asc += nums[i]
        dsc = 0
        for i in range(peak, n):
            dsc += nums[i]
        if asc > dsc:
            return 0
        elif dsc > asc:
            return 1
        else:
            return -1
