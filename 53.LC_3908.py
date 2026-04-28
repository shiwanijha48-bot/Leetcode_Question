class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        N = str(n)
        X = str(x)
        if X in N and N[0] != X:
            return True
        return False
