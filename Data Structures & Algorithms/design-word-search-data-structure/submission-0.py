class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(word: str, root: TrieNode) -> bool:
            curr = root

            for i, ch in enumerate(word):
                if ch not in curr.children:
                    if ch != ".": 
                        return False
                    else:
                        for child in curr.children:
                            if dfs(word[i + 1:], curr.children[child]):
                                return True
                        return False
                curr = curr.children[ch]

            return curr.endOfWord

        return dfs(word, self.root)
