from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        # Start from the end of postorder
        self.post_index = len(postorder) - 1

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None

            # Last element in postorder is the root
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)

            # Get the root's index in inorder
            mid = inorder_index[root_val]

            # IMPORTANT: build right subtree first
            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)

            return root

        return build(0, len(inorder) - 1)


def traverse_bfs(root: Optional[TreeNode]) -> List[int]:
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


if __name__ == "__main__":
    sol = Solution()
    print(traverse_bfs(sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
