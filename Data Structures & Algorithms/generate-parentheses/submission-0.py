class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        substring = ""

        def backtrack(substring: str, left: int, right: int) -> None:
            if len(substring) == (n * 2):
                if substring[0] == "(" and substring[-1] == ")":
                    output.append(substring)
                return

            # Include "("
            if left > 0:
                substring += "("
                backtrack(substring, left - 1, right)
                substring = substring[:-1]

            # Include ")"
            if right > 0 and right > left:
                substring += ")"
                backtrack(substring, left, right - 1)

        backtrack("", n, n)
        return output

        # Time: O(n * 2^n)
        # Space: O(n) - Max substring length, call stack
