from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc = []
        for i in range(numRows):
            arr = []
            if i == 0:
                arr.append(1)
                pasc.append(arr)
                continue
            for j in range(i+1):
                if j == 0 or j == i:
                    arr.append(1)
                else:
                    arr.append(pasc[i-1][j-1]+pasc[i-1][j])
            pasc.append(arr)
        return pasc


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
