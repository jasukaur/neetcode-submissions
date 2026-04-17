class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                op = tokens[i]
                if op == '+':
                    stack.append(n1+n2)
                elif op == '-':
                    stack.append(n2-n1)
                elif op == '*':
                    stack.append(n1*n2)
                else:
                    stack.append(int(float(n2/n1)))
        return stack[-1]