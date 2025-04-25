from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        left, right = 0, len(intervals)
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][1] < newInterval[0]:
                left = mid + 1
            else:
                right = mid
        first = left

        left, right = 0, len(intervals)
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] <= newInterval[1]:
                left = mid + 1
            else:
                right = mid
        last = left

        if first < len(intervals):
            newInterval[0] = min(newInterval[0], intervals[first][0])
        if last > 0:
            newInterval[1] = max(newInterval[1], intervals[last - 1][1])

        return intervals[:first] + [newInterval] + intervals[last:]


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(s.insert(intervals, newInterval))  # Output: [[1,5],[6,9]]
