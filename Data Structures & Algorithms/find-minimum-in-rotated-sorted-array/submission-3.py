class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (nums[0] < nums[-1]) or (len(nums) == 1):
            return nums[0]

        start = 0
        end = len(nums)
        mini = nums[0]

        while start <= end:
            middle = (start+end)//2   
            if nums[middle] >= nums[0]:
                start = middle +1
            else:
                mini = min(mini, nums[middle])
                end = middle - 1

        return mini 
        

