class TrieNode:
    def __init__(self, val: str | None, end: bool = False) -> None:
        self.val = val
        self.end = end
        self.letters = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.letters:
                node = TrieNode(ch)
                curr.letters[ch] = node
                curr = node
            else:
                curr = curr.letters[ch]
        
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.letters:
                return False
            curr = curr.letters[ch]
        
        return curr.end == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.letters:
                return False
            curr = curr.letters[ch]

        return True