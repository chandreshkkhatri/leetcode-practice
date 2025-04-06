
class Solution:
    def countAndSay(self, n: int) -> str:
        countAndSayN = "1"
        # n = 1

        for i in range(n-1):
            counter = 1
            newCountAndSayN = ""
            for j in range(1, len(countAndSayN)):
                if countAndSayN[j] == countAndSayN[j-1]:
                    counter += 1
                else:
                    newCountAndSayN += str(counter) + countAndSayN[j-1]
                    counter = 1
            newCountAndSayN += str(counter) + countAndSayN[-1]
            counter = 1
            countAndSayN = newCountAndSayN

        return countAndSayN


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))
