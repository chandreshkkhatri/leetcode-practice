from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        next_queue = deque()

        while len(queue):
            current_node = queue.popleft()
            for i in range(len(queue)):
                if current_node.left:
                    next_queue.append(current_node.left)
                    next_queue.append(current_node.right)
                next_node = queue.popleft()
                current_node.next = next_node
                current_node = next_node
            if current_node.left:
                next_queue.append(current_node.left)
                next_queue.append(current_node.right)
            queue = next_queue
            next_queue = deque()

        return root


if __name__ == "__main__":
    sol = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    ans = sol.connect(root)
    print(ans)
