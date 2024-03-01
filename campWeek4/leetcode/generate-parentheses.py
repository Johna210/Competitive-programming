class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generate(curr):
            opening_brace = curr.count("(")
            closing_brace = curr.count(")")

            if closing_brace > opening_brace:
                return

            if opening_brace > n:
                return

            if len(curr) == 2*n:
                output.append("".join(curr))
                return
            
            for i in ("(",")"):
                curr.append(i)
                generate(curr)
                curr.pop()

        generate([])
        return output