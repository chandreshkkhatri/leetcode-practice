from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        original_list = []
        current = head

        while current:
            original_list.append(current)
            current = current.next

        copy_list = []

        copy_head = Node(head.val)
        current = head.next
        copy_current = copy_head
        copy_list.append(copy_head)

        while current:
            new_node = Node(current.val)
            copy_current.next = new_node
            copy_list.append(new_node)
            current = current.next
            copy_current = copy_current.next

        copy_current = copy_head
        current = head

        while current:
            if current.random:
                index = original_list.index(current.random)
                copy_current.random = copy_list[index]
            current = current.next
            copy_current = copy_current.next

        return copy_head


if __name__ == "__main__":
    s = Solution()
    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)

    head.random = None
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head

    head = s.copyRandomList(head)
    current = head
    while current:
        print(
            f"Node value: {current.val}, Random value: {current.random.val if current.random else None}")
        current = current.next
