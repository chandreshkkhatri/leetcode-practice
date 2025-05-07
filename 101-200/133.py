"""
# Definition for a Node.
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        new_root = Node(node.val)
        queue = deque([node])
        visited[node] = new_root

        while len(queue):
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]


if __name__ == "__main__":
    s = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print(s.cloneGraph(root))
