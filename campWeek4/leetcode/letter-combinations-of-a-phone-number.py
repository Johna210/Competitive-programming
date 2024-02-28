class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }
        output = []
        def backtrack(path,idx):
            if len(path) == len(digits):
                if path:
                    output.append("".join(path[:]))
                return
            for letter in keyboard[digits[idx]]:
                path.append(letter)
                backtrack(path,idx+1)
                path.pop()

        backtrack([],0)
        return output

