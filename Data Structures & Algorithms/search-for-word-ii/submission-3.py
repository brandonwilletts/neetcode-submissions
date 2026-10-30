class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        output, visited = set(), set()

        root = TrieNode()
        for word in words:
            root.addWord(word)
            
        def dfs(r: int, c: int, root: TrieNode, word: str) -> None:
            if (not(0 <= r < ROWS) or
                not(0 <= c < COLS) or 
                (r, c) in visited or
                board[r][c] not in root.children
            ):
                return
            
            visited.add((r, c))
            word += board[r][c]

            root = root.children[board[r][c]]

            if root.endOfWord:
                output.add(word)

            dfs(r + 1, c, root, word)
            dfs(r - 1, c, root, word)
            dfs(r, c + 1, root, word)
            dfs(r, c - 1, root, word)

            visited.remove((r, c))

        # Search trie for each value in matrix
        for r in range(ROWS):
            for c in range(COLS):
                if len(output) == len(words):
                    return list(output)
                dfs(r, c, root, "")
                
        return list(output)        

        # Time: 
        # Space: 