from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        left = 0
        right = l-1
        max_vol = 0

        while left < right:
            current_vol = min(height[left], height[right])*(right-left)
            max_vol = max(max_vol, current_vol)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol


if __name__ == "__main__":
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    ans = sol.maxArea(height)
    print(ans)
