from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        l = len(triangle)
        min_path_sum = [[0]*i for i in range(1, l+1)]

        for i in range(0, l):
            for j in range(i+1):
                if 0 < j < i:
                    min_path_sum[i][j] = min(
                        min_path_sum[i-1][j-1], min_path_sum[i-1][j]) + triangle[i][j]
                elif j == 0:
                    min_path_sum[i][j] = min_path_sum[i-1][j]+triangle[i][j]
                elif j == i:
                    min_path_sum[i][j] = min_path_sum[i-1][j-1]+triangle[i][j]
        return min(min_path_sum[l-1])


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
