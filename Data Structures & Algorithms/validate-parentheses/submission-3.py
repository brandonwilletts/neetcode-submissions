class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for br in s:
            # Open bracket
            if br in brackets:
                stack.append(br)

            # Closed bracket
            elif not stack or brackets[stack.pop()] != br:
                return False
            
        return not stack

        # Time: O(n)
        # Space: O(n)