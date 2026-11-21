class Node:

    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic: dict[int, Node] = {}
        self.head, self.tail = Node(-1, -1), Node(-2, -2)
        self.head.nxt, self.tail.pre = self.tail, self.head

    def _move_first(self, node: Node):
        if self.head.nxt == node:
            return
        pre, nxt = node.pre, node.nxt
        # detach node
        pre.nxt, nxt.pre = nxt, pre
        # move node to first
        old_head = self.head.nxt
        self.head.nxt = node
        node.pre, node.nxt = self.head, old_head
        old_head.pre = node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self._move_first(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self._move_first(node)
            return
        node = Node(val=value, key=key)
        old_head = self.head.nxt

        self.head.nxt = node
        node.pre, node.nxt = self.head, old_head
        old_head.pre = node

        self.dic[key] = node

        if len(self.dic) > self.capacity:
            last = self.tail.pre
            last.pre.nxt, self.tail.pre = last.nxt, last.pre
            del self.dic[last.key]