from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.traverse(root)
        return self.ans

    def traverse(self, root: Optional[TreeNode]):
        if root:
            self.traverse(root.left)
            self.ans.append(root.val)
            self.traverse(root.right)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(s.inorderTraversal(root))
