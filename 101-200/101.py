from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_queue = deque()
        right_queue = deque()
        left_queue.append(root.left)
        right_queue.append(root.right)

        if not root:
            return True
        if not bool(root.left) and not bool(root.right):
            return True

        if (root.left and not root.right) or (root.right and not root.left):
            return False

        while left_queue and right_queue:
            left_el = left_queue.popleft()
            right_el = right_queue.popleft()
            if left_el.val != right_el.val:
                return False

            if left_el.left:
                left_queue.append(left_el.left)
            if left_el.right:
                left_queue.append(left_el.right)

            if right_el.right:
                right_queue.append(right_el.right)
            if right_el.left:
                right_queue.append(right_el.left)

            if bool(left_el.left) ^ bool(right_el.right):
                return False
            if bool(left_el.right) ^ bool(right_el.left):
                return False

        if (len(left_queue) > 0) or (len(right_queue) > 0):
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(s.isSymmetric(root))  # Output: True
