from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode, depth):
            if not node:
                return 0, True

            depth_left, is_left_bal = dfs(node.left, depth+1)
            depth_right, is_right_bal = dfs(node.right, depth+1)
            return max(depth_left, depth_right)+1, (abs(depth_right-depth_left) < 2) and is_left_bal and is_right_bal

        _, is_bal = dfs(root, 0)

        return bool(is_bal)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(9)
    root.left.left.left = TreeNode(9)
    root.left.left.right = TreeNode(9)

    print(sol.isBalanced(root))
