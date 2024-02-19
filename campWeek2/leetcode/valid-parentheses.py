class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_values = {"}":"{","]":"[",")":"("}

        for i in s:
            if i in dict_values:
                if stack and stack[-1] == dict_values[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False