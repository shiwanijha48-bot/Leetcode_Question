class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        temp = nums
        digit = str(digit)
        count = 0
        for num in temp:
            for ch in str(num):
                if ch == digit:
                    count += 1
        return count
