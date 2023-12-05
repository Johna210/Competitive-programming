class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_line = "qwertyuiop"
        second_line = "asdfghjkl"
        third_line = "zxcvbnm"

        output = []

        for each in words:
            word = each.lower()
            # If the first letter of the first word is on the first line of the keyboard
            if word[0] in first_line:
                valid = True
                # Check wether every letters are on the first line
                for i in range(1,len(word)):
                    if word[i] not in first_line:
                        valid = False
                        break
                if valid:
                    output.append(each)
            # If the first letter of the first word is on the second line of the keyboard
            elif word[0] in second_line:
                valid = True
                # Check wether every letters are on the Second line
                for i in range(1,len(word)):
                    if word[i] not in second_line:
                        valid = False
                        break
                if valid:
                    output.append(each)
            # If the first letter of the first word is on the third line of the keyboard
            elif word[0] in third_line:
                valid = True
                # Check wether every letters are on the Third line
                for i in range(1,len(word)):
                    if word[i] not in third_line:
                        valid = False
                        break
                if valid:
                    output.append(each)

        return output
