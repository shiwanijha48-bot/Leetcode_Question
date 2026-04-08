class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r = []   # empty lst, to store duplicates
        for i in range(0, len(nums)):   # loopeach elemnts in the array
            index = abs(nums[i]) - 1    # convert val-> index, vals from 1 to n, index is 0 to n-1
            if nums[index] < 0:    # check if already visited, negative -> already seen before: it is duplicate
                r.append(abs(nums[i])) # add duplicate to result
            else:
                nums[index] = -nums[index]   # first tym seeing this number, mark it as visited by making it negative
        return r   # return all duplicates

#  TC -> O(n)
#  SC -> O(1)
