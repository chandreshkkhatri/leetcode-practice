class Solution:
    def totalNQueens(self, n: int) -> int:
        results = 0

        def backtrack(row, current_board, cols, diagonals1, diagonals2):
            nonlocal results
            if row == n:
                results += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue

                board_list = list(current_board[row])
                board_list[col] = 'Q'
                new_board = current_board[:row] + \
                    [''.join(board_list)] + current_board[row + 1:]

                backtrack(row + 1, new_board, cols |
                          {col}, diagonals1 | {row - col}, diagonals2 | {row + col})

        empty_board = ['.' * n for _ in range(n)]
        backtrack(0, empty_board, set(), set(), set())

        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))
    print(solution.totalNQueens(5))
    print(solution.totalNQueens(6))
