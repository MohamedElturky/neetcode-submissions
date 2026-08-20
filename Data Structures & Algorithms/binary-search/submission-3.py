class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            n = (left + right)//2
            
            if target == nums[n]:
                return n
            elif target > nums[n]:
                left = n + 1
            else:
                right = n - 1

        return -1