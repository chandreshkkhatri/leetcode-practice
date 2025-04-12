from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if not head:
            return head

        head1 = head
        last = None
        n = 1
        while head.next:
            n += 1
            head = head.next

        head.next = head1
        k = n-k % n
        i = 0

        while not last:
            if i == k:
                last = head
            i += 1
            head = head.next
        new_head = last
        new_head = new_head.next
        last.next = None

        return new_head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    ans = s.rotateRight(head, 2)

    while ans:
        print(ans.val, end=" -> ")
        ans = ans.next
