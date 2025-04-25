from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        maxFromStart = []
        maxFromEnd = []
        currentMaxFromStart = 0
        currentMaxFromEnd = 0
        l = len(height)

        for i in range(l):
            if height[i] > currentMaxFromStart:
                currentMaxFromStart = height[i]
            maxFromStart.append(currentMaxFromStart)
            if height[l - i - 1] > currentMaxFromEnd:
                currentMaxFromEnd = height[l - i - 1]
            maxFromEnd.append(currentMaxFromEnd)

        maxFromEnd.reverse()
        totalWater = 0
        for i in range(l):
            waterLevel = min(maxFromStart[i], maxFromEnd[i])
            if waterLevel > height[i]:
                totalWater += waterLevel - height[i]

        return totalWater


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
