class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # len of row or col(sq matrix)
        for i in range(n):  # transpose of the matrix
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:  # reverse each row
            row.reverse()
#  main intituion = transpose = row into column and then reverse the rows. complete 90 degree rotation
#  TC -> O(n**2)
