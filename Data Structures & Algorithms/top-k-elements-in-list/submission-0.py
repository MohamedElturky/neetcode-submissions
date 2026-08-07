class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        answer = []

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        for lst in reversed(buckets):
            if len(lst) != 0 and k != 0:
                for numb in lst:
                    if k == 0:
                        break
                    else:
                        k-=1
                        answer.append(numb)

        return answer
        