class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:   # root 0 = 0 and root 1 = 1
            return x
        l = 1  # left
        r = x//2  # right rootX is not more than x/2 for x>= 2
        ans = 0
        while l <= r:  # bin search loop
            mid = (l + r)//2   # mid val
            if mid*mid == x: # perfect sq
                return mid
            elif mid*mid < x:  # sq is smaller
                ans = mid # stroe in ans
                l = mid + 1  # try bigger no.
            else:   # sq is big
                r = mid - 1 # move left -> right = mid -1
        return ans  # floor val of rootx
#  TC -> O(n)
