from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            index = inorder_index_map[root_val]

            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    print(s.buildTree([-1], [-1]))
