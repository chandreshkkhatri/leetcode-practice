# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level = []
        ans = []
        next_queue = deque()

        while len(queue):
            for i in range(len(queue)):
                current_node = queue.popleft()
                if current_node.left:
                    next_queue.append(current_node.left)
                if current_node.right:
                    next_queue.append(current_node.right)
                level.append(current_node.val)
            ans.append(level)
            level = []
            queue = next_queue
            next_queue = deque()

        ans.reverse()

        return ans


def buildTree(array):
    if not array:
        return None
    root = TreeNode(array[0])
    queue = deque([root])
    i = 1

    while i < len(array):
        current_node = queue.popleft()
        if array[i] is not None:
            current_node.left = TreeNode(array[i])
            queue.append(current_node.left)
        i += 1
        if i < len(array) and array[i] is not None:
            current_node.right = TreeNode(array[i])
            queue.append(current_node.right)
        i += 1

    return root


if __name__ == "__main__":
    sol = Solution()
    print(sol.levelOrderBottom(buildTree([3, 9, 20, None, None, 15, 7])))
