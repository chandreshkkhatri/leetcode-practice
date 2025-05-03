# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nums = []

        def dfs(node: TreeNode, digits: List[int]) -> None:
            if not node:
                return
            digits.append(node.val)
            if not node.left and not node.right:
                num = int(''.join(map(str, digits)))
                nums.append(num)
                return

            dfs(node.left, digits[:])
            dfs(node.right, digits[:])

        dfs(root, [])
        return sum(nums)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(s.sumNumbers(root))
