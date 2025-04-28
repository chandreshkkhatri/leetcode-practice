from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        next_queue = deque()

        while len(queue):
            current_node = queue.popleft()

            for i in range(len(queue)):
                if current_node.left:
                    next_queue.append(current_node.left)
                if current_node.right:
                    next_queue.append(current_node.right)

                next_node = queue.popleft()
                current_node.next = next_node
                current_node = next_node

            if current_node.left:
                next_queue.append(current_node.left)
            if current_node.right:
                next_queue.append(current_node.right)

            queue = next_queue
            next_queue = deque()

        return root


def levelOrderTraversal(root: Optional[Node]) -> List[int]:
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
            if not node.next:
                result.append(None)

    return result


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)

    solution = Solution()
    print(levelOrderTraversal(solution.connect(root)))
