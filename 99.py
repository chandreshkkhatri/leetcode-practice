from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node1, node2, prev = None, None, None

        def dfs(current: Optional[TreeNode]) -> None:
            nonlocal node1, node2, prev
            if not current:
                return

            dfs(current.left)

            if prev and prev.val > current.val:
                if not node1:
                    node1 = prev
                node2 = current

            prev = current

            dfs(current.right)

        dfs(root)

        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)

    s.recoverTree(root)
