# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.node_stack = []
        self.current = root

    def next(self) -> int:
        # Go as left as possible
        while self.current:
            self.node_stack.append(self.current)
            self.current = self.current.left

        # Pop the node to process it
        node = self.node_stack.pop()
        value = node.val

        # Move to the right subtree
        self.current = node.right

        return value

    def hasNext(self) -> bool:
        return self.current is not None or len(self.node_stack) > 0


if __name__ == "__main__":
    # Example usage:
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15, TreeNode(9), TreeNode(20))

    iterator = BSTIterator(root)

    while iterator.hasNext():
        print(iterator.next())  # Should print the values in ascending order
