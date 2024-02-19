class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ('+','-','*','/'):
                right = int(stack.pop())
                left = int(stack.pop())

                if t == '+':
                    val = left + right
                elif t == '-':
                    val = left - right
                elif t == '*':
                    val = left * right
                else:
                    val = int(left / right)

                stack.append(str(val))
            else:
                stack.append(t)
        return int(stack[0])