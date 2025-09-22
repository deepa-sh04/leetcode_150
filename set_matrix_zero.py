"""
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
This function modifies a matrix in-place so that if any element is 0, the entire row and column of that element become 0.

Step-by-step (short):
Find zeros:
Loop through the matrix.
Store the row indices in rows and column indices in cols whenever a 0 is found.
Zero out rows:
For every row index in rows, set the entire row to 0.
Zero out columns:
For every column index in cols, set the entire column to 0.
So the sets rows and cols record where zeros are, and the final two loops overwrite those rows and columns with zeros.
Complexity:

Time: O(m × n) (scan once + zeroing loops).

Space: O(m + n) (to store row and column indices).
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        row_begin=0
        row_end=len(matrix)-1
        col_begin=0
        col_end=len(matrix[0])-1
        while row_begin<=row_end and col_begin<=col_end:
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin+=1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end-=1
            if row_begin<=row_end:
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end-=1
            if col_begin<=col_end:
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin+=1
        return res                            
