class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        temp = n
        rev = int(str(n)[::-1]) # rev a num
        s = min(temp, rev)  # setting the range
        l = max(temp, rev)
        def primeNo(num):  # function to find out prime nums
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5)+ 1):
                if num % i == 0:
                    return False
            return True
        ans = 0
        for num in range(s, l +1): # check nums in ranege
            if primeNo(num):
                ans = ans +  num  # if prime then add
        return ans
