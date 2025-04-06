from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        empty = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[i//3][j//3].add(val)

        def backtrack(index=0):
            if index == len(empty):
                return True

            i, j = empty[index]
            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[i//3][j//3]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[i//3][j//3].add(num)

                    if backtrack(index + 1):
                        return True

                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[i//3][j//3].remove(num)

            return False

        backtrack()
        print(board)  # For debugging purposes


if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
