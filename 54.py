from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        path = []
        it_row = left
        it_column = up

        if right == 0:
            while it_row <= down:
                path.append(matrix[it_row][it_column])
                it_row += 1
            return path

        while True:
            not_modified = True
            while it_column < right:
                not_modified = False
                path.append(matrix[it_row][it_column])
                it_column += 1
            # path.append(matrix[it_row][it_column])
            up += 1
            if not_modified:
                break
            else:
                not_modified = True

            while it_row < down:
                not_modified = False
                path.append(matrix[it_row][it_column])
                it_row += 1
            # path.append(matrix[it_row][it_column])
            right -= 1
            if not_modified:
                break
            else:
                not_modified = True

            while it_column > left:
                not_modified = False
                path.append(matrix[it_row][it_column])
                it_column -= 1
            # path.append(matrix[it_row][it_column])
            down -= 1
            if not_modified:
                break
            else:
                not_modified = True

            while it_row > up:
                not_modified = False
                path.append(matrix[it_row][it_column])
                it_row -= 1
            # path.append(matrix[it_row][it_column])
            left += 1
            if not_modified:
                break
            else:
                not_modified = True

        path.append(matrix[it_row][it_column])

        return path


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
