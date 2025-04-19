from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ln1 = ListNode(-1)
        ln2 = ListNode(-1)

        node = head
        node1 = ln1
        node2 = ln2

        while node:
            if node.val < x:
                node1.next = node
                node1 = node1.next
            else:
                node2.next = node
                node2 = node2.next

            node = node.next

        node1.next = ln2.next
        node2.next = None

        return ln1.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    ans = sol.partition(head, 3)

    while ans:
        print(ans.val)
        ans = ans.next
