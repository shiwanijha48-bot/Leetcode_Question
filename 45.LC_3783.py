class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev_str = str(n)[::-1]   # int to str and rev
        rev = int(rev_str)  # rev to int
        return abs(n - rev)  # org - rev and its abs as res
