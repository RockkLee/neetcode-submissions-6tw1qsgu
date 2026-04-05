class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        dq = deque()
        operators = {"+", "-", "*", "/"}
        for _, token in enumerate(tokens):
            if token not in operators:
                dq.append(token)
            else:
                num2, num1 = int(dq.pop()), int(dq.pop())
                val = None
                if token == "+":
                    val = num1 + num2
                elif token == "-":
                    val = num1 - num2
                elif token == "*":
                    val = num1 * num2
                elif token == "/":
                    val = int(num1 / num2)
                dq.append(val)
        ans = dq[-1]
        if ans == 0.0:
            return 0
        else:
            return ans

