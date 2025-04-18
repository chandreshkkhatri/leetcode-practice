from typing import List


class Solution:
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
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    print(sol.largestRectangleArea(heights))  # Output: 10
