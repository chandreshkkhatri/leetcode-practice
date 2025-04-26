from typing import Optional
from helpers.tree_helpers import levelOrderTraversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        prev = TreeNode()
        node = TreeNode(root.val, None, None)
        prev.right = node

        def pre_order_traversal(current: Optional[TreeNode]):
            nonlocal node
            if current is None:
                return
            node.right = TreeNode(current.val, None, None)
            node = node.right
            if current.left:
                pre_order_traversal(current.left)
            if current.right:
                pre_order_traversal(current.right)

        pre_order_traversal(root)
        root.right = prev.right.right.right
        root.left = None


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    sol.flatten(root)
    print(levelOrderTraversal(root))
