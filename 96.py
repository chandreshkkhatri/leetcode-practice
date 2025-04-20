

class Solution:
    mem = []

    def numTrees(self, n: int) -> int:
        memo = {}

        def num_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            if start > end:
                return 1

            trees = 0
            for root in range(start, end + 1):
                left_trees = num_trees(start, root - 1)
                right_trees = num_trees(root + 1, end)
                trees += left_trees * right_trees

            memo[(start, end)] = trees
            return trees

        return num_trees(1, n)


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(5))
