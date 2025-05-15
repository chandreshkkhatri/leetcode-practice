# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))  # New dummy head for sorted list
        current = head

        while current:
            prev = dummy
            next_node = current.next  # Save next node

            # Find position to insert current node
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            # Move to next node in original list
            current = next_node

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    print(s.insertionSortList(head))
