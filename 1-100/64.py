from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        memo = {}

        m = len(grid)
        n = len(grid[0])

        def get_sum_from_i_n_j(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m-1 and j == n-1:
                memo[(i, j)] = grid[i][j]
                return grid[i][j]
            elif i == m-1:
                sum_from_i_n_j = grid[i][j]+get_sum_from_i_n_j(
                    i, j+1)
                memo[(i, j)] = sum_from_i_n_j
                return sum_from_i_n_j
            elif j == n-1:
                sum_from_i_n_j = grid[i][j] + get_sum_from_i_n_j(
                    i+1, j)
                memo[(i, j)] = sum_from_i_n_j
                return sum_from_i_n_j
            else:
                sum_1 = grid[i][j]+get_sum_from_i_n_j(i, j+1)
                sum_2 = grid[i][j]+get_sum_from_i_n_j(i+1, j)
                memo[(i, j)] = min(sum_1, sum_2)
                return memo[(i, j)]

        return get_sum_from_i_n_j(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
