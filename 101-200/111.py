from collections import deque
from typing import Optional
from helpers.tree_helpers import buildTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        next_queue = deque()
        queue.append(root)
        depth = 0

        while len(queue):
            depth += 1
            for i in range(len(queue)):
                current_node = queue.pop()
                if not current_node.left and not current_node.right:
                    next_queue = deque()
                    break
                if current_node.left:
                    next_queue.append(current_node.left)
                if current_node.right:
                    next_queue.append(current_node.right)
            queue = next_queue
            next_queue = deque()

        return depth


if __name__ == "__main__":
    s = Solution()
    print(s.minDepth(buildTree([3, 9, 20, None, None, 15, 7])))
