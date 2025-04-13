from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}

        def pathsFromIAndJ(i, j):
            if obstacleGrid[i][j] == 1:
                return 0

            if i == m - 1:
                memo[(i, j)] = int(sum([(1-obstacleGrid[m-1][k])
                                        for k in range(j, n)])/(n-j))
                return memo[(i, j)]
            if j == n - 1:
                memo[(i, j)] = int(sum([(1-obstacleGrid[k][n-1])
                                        for k in range(i, m)])/(m-i))
                return memo[(i, j)]
            if obstacleGrid[i+1][j] == 1 and obstacleGrid[i][j+1] == 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = (1-obstacleGrid[i+1][j])*pathsFromIAndJ(i+1,
                                                                   j) + (1-obstacleGrid[i][j+1])*pathsFromIAndJ(i, j+1)
            return memo[(i, j)]

        return pathsFromIAndJ(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
