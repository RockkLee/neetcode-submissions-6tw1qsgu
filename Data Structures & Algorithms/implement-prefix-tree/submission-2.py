class PrefixTree:

    def __init__(self):
        self.children: dict[str, PrefixTree] = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for _, s in enumerate(word):
            if s not in node.children:
                node.children[s] = PrefixTree()
            node = node.children[s]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for _, s in enumerate(word):
            if s not in node.children:
                return False
            node = node.children[s]
        if not node.is_end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self
        for _, s in enumerate(prefix):
            if s not in node.children:
                return False
            node = node.children[s]
        return True
