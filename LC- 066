class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1): # right se left, last index se start
            if digits[i] < 9:  # 9 se small
                digits[i] += 1  # simply add 1
                return digits  # return then there
            digits[i] = 0   # else- digit 9 tha, then last digit= 0 now
        return [1] + digits  # loop complete, means all where 9 only, so + 1
    #  TC -> O(n)
    #  SC -> O(1)
