from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def levelOrderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result
