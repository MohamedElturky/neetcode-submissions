class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start+end)//2

            if nums[middle] == target:
                return middle

            if nums[start] <= nums[middle]:
                if (target >= nums[start]) and (target < nums[middle]):
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if (target <= nums[end]) and (target > nums[middle]):
                    start = middle + 1
                else:
                    end = middle - 1

        return -1