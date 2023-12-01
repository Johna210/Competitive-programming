class Solution:
    def interpret(self, command: str) -> str:
        val = ""
        left = 0
        dict_values = {"G":"G","()":"o","(al)":"al"}
        while left < len(command):
            if command[left] == "G":
                val += "G"
            elif command[left] == "(":
                substring = "("
                for i in range(left+1,len(command)):
                    substring += command[i]
                    if command[i] == ")":
                        break

                val += dict_values[substring]
            left += 1
        return val
                        