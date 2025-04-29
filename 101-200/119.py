from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i = 0
        row = [1]
        if rowIndex == 0:
            return row
        while i <= rowIndex:
            newRow = [1]
            for j in range(i-1):
                newRow.append(row[j] + row[j+1])
            newRow.append(1)
            row = newRow
            i += 1
        return row


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
