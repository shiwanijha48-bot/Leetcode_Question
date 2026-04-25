class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        blank = moves.count('_')
        ans = abs(left- right) + blank
        return ans

#  Basic solution= Total left, total right it moved, check max in both. 
# then absolute gives the max step in any one of the dirention. 
# so just add blank and get the maximum steps you can go in any of the direction.
