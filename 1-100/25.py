from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        prev = ListNode()
        prev.next = head

        current = head
        while i < k and current.next:
            i += 1
            current = current.next
        if i < k-1:
            return head

        nxt = head.next
        head.next = None
        current = head
        i = 1

        while i < k:
            tmp = nxt.next
            nxt.next = current
            current = nxt
            nxt = tmp
            i += 1

        head.next = nxt
        tmp = head
        head = current
        current = tmp

        while nxt:
            i = 0

            prev = current
            current = nxt
            first = current
            while i < k and current.next:
                i += 1
                current = current.next
            if i < k-1:
                return head

            nxt = first.next
            first.next = None
            current = first
            i = 1

            while i < k:
                tmp = nxt.next
                nxt.next = current
                current = nxt
                nxt = tmp
                i += 1

            tmp = first
            first.next = nxt
            first = nxt
            prev.next = current
            current = tmp

        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    ans = s.reverseKGroup(head, 2)

    while ans:
        print(ans.val)
        ans = ans.next
