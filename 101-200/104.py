from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 1
        result = []

        while stack:
            el, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth

            if el.right:
                stack.append((el.right, depth+1))
            if el.left:
                stack.append((el.left, depth+1))

        return max_depth


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(s.maxDepth(root))
