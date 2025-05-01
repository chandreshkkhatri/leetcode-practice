from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Recursively compute max path sum for left and right
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Path sum including both children and current node
            price_newpath = node.val + left_gain + right_gain

            # Update global max sum if this is better
            self.max_sum = max(self.max_sum, price_newpath)

            # Return max gain (only one side can be chosen to continue the path)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    ans = sol.maxPathSum(root)
    print(ans)
