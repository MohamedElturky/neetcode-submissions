class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        area = 0

        while start < end:
            area = max(area, (end-start) * (min(heights[start],heights[end])))
            if heights[start] > heights[end]:
                end-=1
            else:
                start+=1
        
        return area
