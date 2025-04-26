from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        target = targetSum
        if not root:
            return []

        def dfs(current_path, node, target, current_sum):
            if (not node.left and not node.right) and (current_sum == target):
                results.append(current_path)
            if node.left:
                dfs(current_path+[node.left.val], node.left,
                    target, current_sum+node.left.val)
            if node.right:
                dfs(current_path+[node.right.val], node.right,
                    target, current_sum+node.right.val)

        dfs([root.val], root, target, root.val)
        return results


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
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    print(sol.pathSum(root, 22))
