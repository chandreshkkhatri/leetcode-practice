# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 0:
            return
        if l == 1:
            return lists[0]
        if l == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = l//2
            l1 = self.mergeKLists(lists[:mid])
            l2 = self.mergeKLists(lists[mid:])
            return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        list3_head = list3

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    list3.next = ListNode(list1.val)
                    list3 = list3.next
                    list1 = list1.next
                else:
                    list3.next = ListNode(list2.val)
                    list3 = list3.next
                    list2 = list2.next
            else:
                if list1:
                    list3.next = ListNode(list1.val)
                    list3 = list3.next
                    list1 = list1.next
                else:
                    list3.next = ListNode(list2.val)
                    list3 = list3.next
                    list2 = list2.next

        return list3_head.next


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    ans = sol.mergeKLists([l1, l2, l3])

    while ans:
        print(ans.val)
        ans = ans.next
