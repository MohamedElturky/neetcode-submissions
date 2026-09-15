class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        mini = end
        if len(piles) == h:
            return end

        while start <= end:
            middle = (start+end)//2
            time = 0
            for num in piles:
                time+=(num + middle - 1)//middle
            if time > h:
                start = middle + 1
            else:
                mini = min(mini, middle)
                end = middle - 1

        return mini
