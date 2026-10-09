class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        operators = set(["+", "-", "*", "/"])
        stack = []

        for t in tokens:
            if t in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                match t:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(num1 / num2)
            else:                    
                stack.append(t)
        
        return int(stack.pop())