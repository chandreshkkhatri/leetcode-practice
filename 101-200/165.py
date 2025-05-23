class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split(".")
        list2 = version2.split(".")

        l1 = len(list1)
        l2 = len(list2)

        max_l = max(l1, l2)

        while len(list1) > len(list2):
            list2.append('0')
        while len(list2) > len(list1):
            list1.append('0')

        i = 0
        while i < max_l:
            if int(list1[i]) > int(list2[i]):
                return 1
            elif int(list1[i]) < int(list2[i]):
                return -1
            i += 1

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("1.10", "1.1"))
