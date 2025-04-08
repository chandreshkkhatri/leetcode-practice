from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        p = 0
        n = len(matrix)
        for p in range(n//2):
            for i in range(n-1-p*2):
                (matrix[p][p+i], matrix[n-1-p-i][p], matrix[n-1-p][n-1-p-i], matrix[p+i][n-1-p]) = (
                    matrix[n-1-p-i][p], matrix[n-1-p][n-1-p-i], matrix[p+i][n-1-p], matrix[p][p+i])


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)
    print(matrix)
