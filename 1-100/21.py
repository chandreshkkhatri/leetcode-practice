# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        list3_head = list3

        while list1 and list2:
            if list1.val < list2.val:
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next

        while list1:
            list3.next = ListNode(list1.val)
            list3 = list3.next
            list1 = list1.next
        while list2:
            list3.next = ListNode(list2.val)
            list3 = list3.next
            list2 = list2.next

        return list3_head.next


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ans = sol.mergeTwoLists(l1, l2)

    while ans:
        print(ans.val)
        ans = ans.next
