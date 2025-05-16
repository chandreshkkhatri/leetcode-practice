# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Extract values
        node = head
        values = []
        while node:
            values.append(node.val)
            node = node.next

        # Step 2: Sort values
        values.sort()

        # Step 3: Create a new sorted linked list
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    print(s.sortList(head))
