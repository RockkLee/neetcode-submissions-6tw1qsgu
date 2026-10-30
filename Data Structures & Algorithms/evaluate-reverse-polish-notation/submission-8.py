class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        calc_signs = {"+", "-", "*", "/"}
        for s in tokens:
            if s in calc_signs:
                b = stack.pop()
                a = stack.pop()
                if s == "+":
                    stack.append(a + b)
                elif s == "-":
                    stack.append(a - b)
                elif s == "*":
                    stack.append(a * b)
                else : # "/"
                    stack.append(int(a / b))
                continue
            stack.append(int(s))
        return stack[-1]