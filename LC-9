class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:   # negatuve number 
            return False
        rev = 0
        temp = x
        while x > 0:  # positive number
            ld = x % 10   
            rev = rev * 10 + ld
            x = x // 10
        if temp == rev:
            return True
        else:
            return False
#  TC -> O(N)
#  SC -> O(1)
