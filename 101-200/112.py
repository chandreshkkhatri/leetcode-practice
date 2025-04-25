from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        root.sum = root.val
        self.hasPath = False
        self.helper(root, 0, targetSum)
        return self.hasPath

    def helper(self, node, _sum, targetSum):
        if not node:
            return
        node.sum = _sum + node.val
        if not node.left and not node.right:
            if node.sum == targetSum:
                self.hasPath = True
        else:
            self.helper(node.left, node.sum, targetSum)
            if self.hasPath:
                return
            self.helper(node.right, node.sum, targetSum)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    ans = sol.hasPathSum(root, 22)
    print(ans)
