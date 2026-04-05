class Trie:
    def __init__(self):
        self.children: dict[str, 'Trie'] = {}
        self.is_end: bool = False


class WordDictionary:

    def __init__(self):
        self.root_trie = Trie()

    def addWord(self, word: str) -> None:
        node = self.root_trie
        for _, s in enumerate(word):
            if s not in node.children:
                node.children[s] = Trie()
            node = node.children[s]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.__find(self.root_trie, word)

    def __find(self, trie: Trie, word: str) -> bool:
        node = trie
        for idx, s in enumerate(word):
            if s == ".":
                if idx == len(word) - 1:
                    for child in node.children.values():
                        if child.is_end: return True
                    return False
                for child in node.children.values():
                    if self.__find(child, word[idx + 1:]): return True
            if s not in node.children:
                return False
            node = node.children[s]
            if not node.children and idx < len(word) - 1:
                return False
        return True if node.is_end else False