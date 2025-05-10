from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        node = head
        q = deque()

        while node:
            q.append(node)
            node = node.next

        node = q.popleft()
        while q:
            node.next = q.pop()
            node = node.next
            if q:
                node.next = q.popleft()
                node = node.next

        node.next = None  # Terminate list properly


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s.reorderList(head)

    current = head
    while current:
        print(current.val)
        current = current.next
