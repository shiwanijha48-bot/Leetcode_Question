class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        b = bin(n)[2:] # int to bin, removing 0b by slicing
        ans = ""
        for ch in b:  # reversing the chars
            if ch == '0':
                ans += '1'
            else:
                ans += '0'
        return int(ans,2)  # again bin to int
