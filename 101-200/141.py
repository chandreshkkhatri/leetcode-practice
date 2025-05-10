# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        nodeList = []
        while current and current.next:
            if current in nodeList:
                return True
            nodeList.append(current)
            current = current.next

        return False


if __name__ == "__main__":
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(s.hasCycle(head))
