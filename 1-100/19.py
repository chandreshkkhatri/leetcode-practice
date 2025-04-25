# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        l = 0

        while node:
            node = node.next
            l += 1

        node = head
        idx_from_start = l - n
        if idx_from_start == 0:
            return node.next

        for i in range(idx_from_start-1):
            node = node.next

        if node.next:
            node.next = node.next.next

        return head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
