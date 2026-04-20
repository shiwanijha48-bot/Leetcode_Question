class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []  # lst for store count of each node
        for row in matrix: # each row traverse
            count = 0 # count edge
            for val in row: # adj mat each row ki val, 0 or 1
                if val == 1: # 1 means edge there, so cnt increase
                    count += 1
            ans.append(count)  # in lst for each node
        return ans

#  basic idea= har vertex ke liye uski adj row me jitne 1 h, utna return krna h kyonki vo uske edges connection count h.
#  TC -> o(n^2)
#  SC -> o(n) = lst of ans
