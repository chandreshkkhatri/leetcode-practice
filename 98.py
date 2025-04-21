from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=float('-inf'), ceiling=float('inf')) -> bool:
        if not root:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False

        if self.isValidBST(root.left, floor, ceiling=root.val) and self.isValidBST(root.right, root.val, ceiling):
            return True

        return False


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.isValidBST(root))
