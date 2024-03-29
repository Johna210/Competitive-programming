class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = digits = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                stack.append(int(digits)*substr)
        return "".join(stack)