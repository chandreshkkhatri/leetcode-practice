from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(-200)
        current.next = head

        while current.next:
            if (current.val != current.next.val):
                current = current.next
            else:
                current.next = current.next.next
        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    ans = s.deleteDuplicates(head)

    while ans:
        print(ans.val)
        ans = ans.next
