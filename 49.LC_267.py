class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num  # range from 1 to num(possible sq roots)
        while left <= right:  # binary search until range is valid
            mid = (left + right) // 2  # middle val
            sq = mid * mid  
            if sq == num:   # if matches, return true
                return True
            elif sq < num:   # sq is smaller, move right(inc value)
                left = mid + 1
            else:    # sq is larger, move left (dec val)
                right = mid - 1
        return False   # if no val found -> not a perfect sq
