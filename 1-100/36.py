from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tally_rows = [[0]*9 for j in range(9)]
        tally_cols = [[0]*9 for j in range(9)]
        tally_block = [[0]*9 for j in range(9)]

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != '.':
                    col = int(col)-1
                    if tally_rows[i][col] == 0:
                        tally_rows[i][col] = 1
                    else:
                        return False

                    if tally_cols[j][col] == 0:
                        tally_cols[j][col] = 1
                    else:
                        return False

                    if i < 3:
                        if j < 3:
                            if tally_block[0][col] == 0:
                                tally_block[0][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                        elif j < 6:
                            if tally_block[1][col] == 0:
                                tally_block[1][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                        elif j < 9:
                            if tally_block[2][col] == 0:
                                tally_block[2][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                    elif i < 6:
                        if j < 3:
                            if tally_block[3][col] == 0:
                                tally_block[3][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                        elif j < 6:
                            if tally_block[4][col] == 0:
                                tally_block[4][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                        else:
                            if tally_block[5][col] == 0:
                                tally_block[5][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                    else:
                        if j < 3:
                            if tally_block[6][col] == 0:
                                tally_block[6][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                        elif j < 6:
                            if tally_block[7][col] == 0:
                                tally_block[7][col] = 1
                            else:
                                # print('b', i, j)
                                return False
                        else:
                            if tally_block[8][col] == 0:
                                tally_block[8][col] = 1
                            else:
                                # print('b', i, j)
                                return False

        return True


if __name__ == "__main__":
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(s.isValidSudoku(board))
