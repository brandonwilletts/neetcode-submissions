class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        part = []

        def dfs(i: int) -> None:
            if i >= len(s):
                output.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return output

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

        # Time: O(n * 2^n)
        # Space: O(n) - Max substring, call stack
