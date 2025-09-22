"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

The code rotates a square matrix 90° clockwise in two steps:
Transpose:
Swap elements across the diagonal so rows become columns.
Example → [[1,2,3],[4,5,6],[7,8,9]] → [[1,4,7],[2,5,8],[3,6,9]].
Reverse each row:
Flip every row horizontally to complete the clockwise rotation.
Result → [[7,4,1],[8,5,2],[9,6,3]].
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix    
