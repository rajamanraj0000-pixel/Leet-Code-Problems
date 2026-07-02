class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        r_track = [0 for _ in range(rows)]
        c_track = [0 for _ in range(columns)]

        for i in range(0,rows):
            for j in range(0,columns):
                if matrix[i][j] == 0:
                    r_track[i] = -1
                    c_track[j] = -1

        for i in range(0,rows):
            for j in range(0,columns):
                if r_track[i] == -1 or c_track[j] == -1:
                    matrix[i][j] = 0
        