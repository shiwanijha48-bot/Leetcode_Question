class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = s + s
        if len(s) != len(goal):
            return False
        if goal in temp:
            return True
        else:
            return False
#  main intuition trick-
#  rotation = shifting characters
#  s + s = contains all shifts
