from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        height_matrix = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0:
                        height_matrix[i][j] = 1
                    else:
                        height_matrix[i][j] = height_matrix[i-1][j]+1
        max_area = 0

        for i in range(m):
            max_row_area = self.largestRectangleArea(height_matrix[i])
            max_area = max(max_area, max_row_area)

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)

        return max_area


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    sol = Solution()
    print(sol.maximalRectangle(matrix))  # Output: 6
