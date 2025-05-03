from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1 or board[r][c] != 'O':
                return

            print(board)
            board[r][c] = 'S'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(m):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][n-1] == 'O':
                dfs(r, n-1)

        for c in range(n):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[m-1][c] == 'O':
                dfs(m-1, c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == "__main__":
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(board)
    print(board)
