from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if len(word) > m*n:
            return False

        for i in range(m):
            for j in range(n):
                if self.is_valid_word_start(board, word, i, j):
                    return True

        return False

    def is_valid_word_start(self, board, word, row, col):

        def backtrack(current_str, used_cells, i, j, word, board):
            if len(current_str) == len(word):
                return True

            str_len = len(current_str)

            if i > 0 and (i-1, j) not in used_cells and board[i-1][j] == word[str_len]:
                used_cells.add((i-1, j))
                if (backtrack(current_str+board[i-1][j], used_cells, i-1, j, word, board)):
                    return True
                used_cells.remove((i-1, j))

            if j > 0 and (i, j-1) not in used_cells and board[i][j-1] == word[str_len]:
                used_cells.add((i, j-1))
                if (backtrack(current_str+board[i][j-1], used_cells, i, j-1, word, board)):
                    return True
                used_cells.remove((i, j-1))

            if i < len(board)-1 and (i+1, j) not in used_cells and board[i+1][j] == word[str_len]:
                used_cells.add((i+1, j))
                if (backtrack(current_str+board[i+1][j], used_cells, i+1, j, word, board)):
                    return True
                used_cells.remove((i+1, j))

            if j < len(board[0]) - 1 and (i, j+1) not in used_cells and board[i][j+1] == word[str_len]:
                used_cells.add((i, j+1))
                if (backtrack(current_str+board[i][j+1], used_cells, i, j+1, word, board)):
                    return True
                used_cells.remove((i, j+1))

        if board[row][col] == word[0]:
            return (backtrack(word[0], set([(row, col)]), row, col, word, board))


if __name__ == "__main__":
    board = [["a", "a"], ["A", "A"]]
    word = "aaa"
    print(Solution().exist(board, word))
