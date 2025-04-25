class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = 'down'
        row_num = 0
        lists = [[] for i in range(len(s))]
        if numRows == 1:
            return s
        for c in s:
            if direction == 'down':
                lists[row_num].append(c)
                if row_num == numRows-1:
                    direction = 'up'
                    row_num -= 1
                else:
                    row_num += 1
            else:
                lists[row_num].append(c)
                if row_num == 0:
                    direction = 'down'
                    row_num = 1
                else:
                    row_num -= 1

        new_s = ''
        for _list in lists:
            new_s += ''.join(_list)
        return new_s


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
