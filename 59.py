from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        up, down = 0, n - 1

        row, col = 0, 0
        it = 1

        while it <= n * n:
            while col <= right and it <= n * n:
                matrix[row][col] = it
                it += 1
                col += 1
            col -= 1
            row += 1
            up += 1

            while row <= down and it <= n * n:
                matrix[row][col] = it
                it += 1
                row += 1
            row -= 1
            col -= 1
            right -= 1

            while col >= left and it <= n * n:
                matrix[row][col] = it
                it += 1
                col -= 1
            col += 1
            row -= 1
            down -= 1

            while row >= up and it <= n * n:
                matrix[row][col] = it
                it += 1
                row -= 1
            row += 1
            col += 1
            left += 1

        return matrix


if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.generateMatrix(n))  # Output: [[1,2,3],[8,9,4],[7,6,5]]
