from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval_min = pow(10, 4)
        interval_max = 0
        for interval in intervals:
            if interval[0] < interval_min:
                interval_min = interval[0]
            if interval[1] > interval_max:
                interval_max = interval[1]

        interval_map = [{"intervals_started": 0,
                         "intervals_ended": 0} for _ in range(interval_max - interval_min + 1)]

        for interval in intervals:
            interval_map[interval[0]-interval_min]["intervals_started"] += 1
            interval_map[interval[1] - interval_min]["intervals_ended"] += 1

        ans = []
        current_interval = [-1, -1]
        running_intervals = 0

        for idx, interval_events in enumerate(interval_map):
            if not running_intervals and interval_events["intervals_started"]:
                current_interval[0] = idx + interval_min
            running_intervals += interval_events["intervals_started"]
            running_intervals -= interval_events["intervals_ended"]
            if not running_intervals and interval_events["intervals_ended"]:
                current_interval[1] = idx + interval_min
                ans.append(current_interval[:])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
