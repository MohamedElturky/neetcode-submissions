class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break
            
            j = i+1
            k = len(nums)-1
            while k > j:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                    while j < k and nums[j] == nums[j - 1]:
                        j+=1
                    while j < k and nums[k] == nums[k + 1]:
                        k-=1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k-=1
                else:
                    j+=1

        return ans