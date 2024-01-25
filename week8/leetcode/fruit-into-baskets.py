class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        max_count = 0
        left = 0
        total = 0

        for index in range(len(fruits)):
            basket[fruits[index]] += 1
            total += 1
                
            while len(basket) > 2:
                f = fruits[left]
                basket[f] -= 1
                total -= 1
                left+=1
                if not basket[f]:
                    basket.pop(f)

            max_count = max(max_count,total)

        return max_count