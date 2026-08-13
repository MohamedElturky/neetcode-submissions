class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxi = 0
        for num in numbers:
            if num - 1 in numbers:
                continue
            else:
                count = 1
                i = num
                while i + 1 in numbers:
                    i+=1
                    count+=1 
                maxi = max(maxi, count)
        return maxi