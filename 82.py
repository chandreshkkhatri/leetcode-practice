from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(0)
        current.next = head
        pre_node = current

        while current.next:
            hasDuplicate = False

            if current.next.next and (current.next.next.val == current.next.val):
                hasDuplicate = True
            while current.next.next and (current.next.next.val == current.next.val):
                current.next.next = current.next.next.next
            if hasDuplicate:
                current.next = current.next.next
            else:
                current = current.next

        return pre_node.next


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
