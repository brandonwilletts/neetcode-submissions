class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        substring = ""

        def backtrack(substring: str, op: int, cl: int) -> None:
            if len(substring) == (n * 2):
                output.append(substring)
                return

            # Include "("
            if op < n:
                substring += "("
                backtrack(substring, op + 1, cl)
                substring = substring[:-1]

            # Include ")"
            if cl < n and cl < op:
                substring += ")"
                backtrack(substring, op, cl + 1)

        backtrack("", 0, 0)
        return output

        # Time: O(n * 2^n)
        # Space: O(n) - Max substring length, call stack
