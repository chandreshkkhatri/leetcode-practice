class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dictionary = {i: chr(64 + i) for i in range(1, 27)}
        word = ""
        while columnNumber:
            mod = (columnNumber-1) % 26+1
            c = dictionary[mod]
            columnNumber = (columnNumber-1)//26
            word += c

        return word[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(701))
    # print(27//26)
