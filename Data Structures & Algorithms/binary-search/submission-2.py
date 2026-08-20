class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        while len(nums) != 0:
            n = len(nums)//2
            
            if target > nums[n]:
                nums = nums[n+1:]
                index = index + n + 1
            elif target < nums[n]:
                nums = nums[:n]
            else:
                return index + n

        return -1