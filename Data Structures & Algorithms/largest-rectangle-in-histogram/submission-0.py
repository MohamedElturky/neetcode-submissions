class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [0]
        max_area = 0

        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                val = heights[stack.pop()]
                if not stack:
                    left = -1
                else:
                    left = stack[-1]
                width = i - left - 1
                area = val * width
                max_area = max(max_area, area)
            stack.append(i)

        return max_area