from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or matrix == [[]]:
            return matrix
        rows = set()
        columns = set()
        m = len(matrix)
        n = len(matrix[0])
        zeros = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append([i, j])

        for zero in zeros:
            if zero[0] not in rows and zero[1] not in columns:
                for k in range(m):
                    matrix[k][zero[1]] = 0
                for k in range(n):
                    matrix[zero[0]][k] = 0
            elif zero[0] in rows and zero[1] not in columns:
                for k in range(m):
                    matrix[k][zero[1]] = 0
            elif zero[0] not in rows and zero[1] in columns:
                for k in range(n):
                    matrix[zero[0]][k] = 0
            rows.add(zero[0])
            columns.add(zero[1])

        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
