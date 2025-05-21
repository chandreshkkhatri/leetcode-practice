# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set_1 = set()
        nodeA = headA

        while nodeA:
            node_set_1.add(nodeA)
            nodeA = nodeA.next

        nodeB = headB

        while nodeB:
            if nodeB in node_set_1:
                return nodeB
            nodeB = nodeB.next

        return None


if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(1)
    node3 = ListNode(8)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = ListNode(5)
    node7 = ListNode(6)
    node8 = ListNode(1)
    node6.next = node7
    node7.next = node8
    node8.next = node3

    sol = Solution()
    ans = sol.getIntersectionNode(node1, node6)

    print(ans.val)
