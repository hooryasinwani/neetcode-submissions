class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                last = stack.pop()
                secondLast = stack.pop()
                if i == "+":
                    result = last + secondLast
                elif i == "-":
                    result = secondLast - last
                elif i == "*":
                    result = secondLast * last
                elif i == "/":
                    result = int(secondLast/last)
                stack.append(result)
        return stack[-1]
        