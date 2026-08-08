class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        after = [1] * n
        loop = n - 1
        i = 1
        j =  n - 2
        while loop > 0:
            answer[i] = answer[i - 1] * nums[i - 1]
            after[j] = after [j + 1] * nums[j + 1]
            i+=1
            j-=1
            loop-=1

        k = 0
        while k < n:
            answer[k]*=after[k]
            k+=1

        return answer