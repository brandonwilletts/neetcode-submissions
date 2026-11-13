class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjMap = defaultdict(list)

        wordList.append(beginWord)

        # Build adjacency list using patterns
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjMap[pattern].append(word)

        # BFS to find shortest path
        output = 1
        visited = set([beginWord])
        q = deque([beginWord])
        
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return output
                
                # Get and push neighbors
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in adjMap[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            
            output += 1
        
        return 0

        # Time: O(n * m^2)
        # Space: O(n * m^2)
