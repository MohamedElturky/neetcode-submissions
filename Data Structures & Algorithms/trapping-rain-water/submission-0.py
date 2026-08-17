class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        ans = 0
        while l < r:
            if height[l] <= height[r]:
                l+=1
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    ans = ans + (max_l - height[l])
            else:
                r-=1
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    ans = ans + (max_r - height[r])

        return ans
