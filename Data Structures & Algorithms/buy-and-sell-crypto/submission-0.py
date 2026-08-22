class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 101
        max_profite = 0

        for num in prices:
            if num < minimum:
                minimum = num
            else:
                profite = num - minimum
                if profite > max_profite:
                    max_profite = profite

        return max_profite