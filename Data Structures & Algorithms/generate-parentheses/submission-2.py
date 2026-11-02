class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def backtrack(op: int, cl: int) -> None:
            if op == cl == n:
                output.append("".join(stack))
                return

            # Include "("
            if op < n:
                stack.append("(")
                backtrack(op + 1, cl)
                stack.pop()

            # Include ")"
            if cl < n and cl < op:
                stack.append(")")
                backtrack(op, cl + 1)
                stack.pop()

        backtrack(0, 0)
        return output

        # Time: O(2^n)
        # Space: O(n) - Max substring length, call stack
