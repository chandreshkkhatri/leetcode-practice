from collections import deque
from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []

        while (len(queue) > 0):
            current_el = queue.popleft()
            if current_el.left:
                queue.append(current_el.left)
            if current_el.right:
                queue.append(current_el.right)
            ans.append(current_el.val)

        return ans


if __name__ == "__main__":
    s = Solution()
