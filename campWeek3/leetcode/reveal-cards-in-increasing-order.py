class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        output = deque()
        deck.sort(reverse=True)
        output.append(deck[0])

        for i in range(1,len(deck)):
            val = output.pop()
            output.appendleft(val)
            output.appendleft(deck[i])

        return output
