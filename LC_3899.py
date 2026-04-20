# Formula based Question

import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides
        if (a+b) <= c or (b+c)<= a or (a+c) <= b:
            return []
        A = math.degrees(math.acos((b*b + c*c -a*a) / (2*b*c)))
        B = math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))
        C = math.degrees(math.acos((a*a + b*b - c*c) / (2*a*b)))
        ans = [A,B,C]
        ans.sort()
        return ans
# acos() → used to find angle
# degrees() → used to convert radians into degrees
# This is a formula-based question
# Time Complexity → O(1)
# Space Complexity → O(1)
        
