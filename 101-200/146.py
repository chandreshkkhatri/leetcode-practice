class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        self.head = ListNode()  # dummy head
        self.tail = ListNode()  # dummy tail
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode):
        prev_node = node.prev
        next_node = node.nxt
        prev_node.nxt = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: ListNode):
        prev = self.tail.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) == self.capacity:
                # Evict LRU
                lru_node = self.head.nxt
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)


if __name__ == "__main__":
    s = LRUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    print(s.get(1))
    s.put(3, 3)
    print(s.get(2))
    s.put(4, 4)
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))
