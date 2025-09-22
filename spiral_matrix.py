"""
Initialize boundaries
row_begin, row_end → top & bottom row limits.
col_begin, col_end → left & right column limits.
Loop while boundaries remain
Left → Right: traverse top row, then move row_begin down.
Top → Bottom: traverse right column, then move col_end left.
Right → Left: (if rows remain) traverse bottom row, then move row_end up.
Bottom → Top: (if columns remain) traverse left column, then move col_begin right.
Repeat until all elements are added to out.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

This systematically peels the matrix layer by layer in a clockwise spiral.
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
