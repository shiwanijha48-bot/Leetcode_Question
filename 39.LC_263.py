class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:  # ugly num must be positive
            return False
        for i in [2,3,5]:  # checking allowed prime factors
            while n % i == 0:
                n = n // i # dividing n by 2,3,5
        if n == 1:   # if only 2, 3, 5 are factors then n will become 1
            return True
        return False
