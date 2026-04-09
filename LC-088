class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1   # points to last valid elemnt in nums1, extra 0s
        j = n-1   # points to last elemnt in nums2
        k = m + n -1  # points to last position of nums1
        while j >= 0:  # loop until all elemnts of nums2 are placed
            if i >= 0 and nums1[i] > nums2[j]:   # i>=0 avoids index error, compare last elmnts of both arrays
                nums1[k] = nums1[i]   # putting bigger at end
                i -= 1     # move nums1 ptr left
            else:    # if nums2 elemnt is bigger
                nums1[k] = nums2[j]   # place it at end
                j -= 1    # move nums2 ptr left
            k -= 1  # move final position left

#  TC -> O(m+n)
#  SC -> O(1)
