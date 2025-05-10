# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        node = head
        pos = 0

        visited_set = set()

        while node:
            if node in visited_set:
                return node
            visited_set.add(node)
            node = node.next
            pos += 1

        return None


if __name__ == "__main__":
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(s.detectCycle(head))
