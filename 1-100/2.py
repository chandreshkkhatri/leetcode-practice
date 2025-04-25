from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        num1, num2 = 0, 0

        node = l1
        it = 0
        while node:
            num1 += node.val*(10**it)
            it += 1
            node = node.next

        node = l2
        it = 0
        while node:
            num2 += node.val*(10**it)
            it += 1
            node = node.next

        num3 = num1 + num2

        head = ListNode(val=num3 % 10)
        node = head
        num3 //= 10

        while num3:
            node.next = ListNode(val=num3 % 10)
            node = node.next
            num3 //= 10

        return head


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    ans = sol.addTwoNumbers(l1, l2)

    while ans:
        print(ans.val)
        ans = ans.next
