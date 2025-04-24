from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        sorted_list = []
        while node:
            sorted_list.append(node.val)
            node = node.next

        def sorted_list_to_bst(sorted_list):
            if len(sorted_list) == 0:
                return None
            if len(sorted_list) == 1:
                return TreeNode(sorted_list[0])

            l = len(sorted_list)
            mid = l//2

            root = TreeNode(sorted_list[mid])
            root.left = sorted_list_to_bst(sorted_list[:mid])
            root.right = sorted_list_to_bst(sorted_list[mid+1:])

            return root

        return sorted_list_to_bst(sorted_list)


def print_tree_bbfs(root):
    if not root:
        return

    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    print(result)


if __name__ == "__main__":
    s = Solution()
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    ans = s.sortedListToBST(head)

    print_tree_bbfs(ans)
