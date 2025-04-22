from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        next_queue = deque()
        level = []
        right = True

        while len(queue) > 0:
            for i in range(len(queue)):
                el = queue.popleft()
                level.append(el.val)
                if right:
                    if el.left:
                        next_queue.append(el.left)
                    if el.right:
                        next_queue.append(el.right)
                else:
                    if el.right:
                        next_queue.append(el.right)
                    if el.left:
                        next_queue.append(el.left)

            ans.append(level)
            level = []
            queue = next_queue
            queue.reverse()
            next_queue = deque()
            right = not right

        return ans


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(9)
    root.left.left.left = TreeNode(9)
    root.left.left.right = TreeNode(9)

    print(s.zigzagLevelOrder(root))
