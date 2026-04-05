class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev: Node|None = None
        self.next: Node|None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # k: key, v: Node (pointer)

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Node):
        """
        insert a node before the latest node
        """
        self.latest.prev.next = node
        node.next = self.latest
        node.prev = self.latest.prev
        self.latest.prev = node
