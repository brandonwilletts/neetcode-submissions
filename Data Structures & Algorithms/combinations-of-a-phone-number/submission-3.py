LETTERS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        stack = []

        def dfs(i: int) -> None:
            if i == len(digits):
                output.append("".join(stack))
                return

            for ch in LETTERS[digits[i]]:
                stack.append(ch)
                dfs(i + 1)
                stack.pop()

        if digits:
            dfs(0)

        return output

        # Time: O(n * 4^n)
        # Space: O(n) - Max stack size, call stack
