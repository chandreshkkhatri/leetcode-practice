from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(start, end):
            if start == end:
                return matrix[start]
            mid = (start+end)//2
            if matrix[mid][-1] >= target:
                return find_row(start, mid)
            else:
                return find_row(mid + 1, end)

        row = find_row(0, len(matrix)-1)

        def find_target(l, target):
            if len(l) == 1:
                if l[0] == target:
                    return True
                else:
                    return False

            left = 0
            right = len(l) - 1
            mid = (left+right)//2

            if l[mid] == target:
                return True
            if l[mid] > target:
                return find_target(l[left:mid+1], target)
            else:
                return find_target(l[mid+1:right+1], target)

        return find_target(row, target)


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(
        [[1, 1]], 2))
