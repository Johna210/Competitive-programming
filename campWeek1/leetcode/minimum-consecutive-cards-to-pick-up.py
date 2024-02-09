class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = len(cards) + 1
        left = 0
        card_count = defaultdict(int)

        for right in range(len(cards)):
            card_count[cards[right]] += 1

            while card_count[cards[right]] >= 2:
                min_len = min(min_len,right-left+1)
                card_count[cards[left]] -= 1
                left+=1

        return min_len if min_len < len(cards)+1 else -1