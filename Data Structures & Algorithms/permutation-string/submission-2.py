class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        n = len(s1)

        for c in s1:
            if c in dic:
                dic[c]+=1
            else:
                dic[c] = 1

        start = 0

        for i in range(len(s2)):
            if s2[i] in dic:
                dic[s2[i]]-=1
                while dic[s2[i]] == -1:
                    if s2[start] in dic:
                        dic[s2[start]]+=1
                    start+=1
            else:
                while start != i+1:
                    if s2[start] in dic:
                        dic[s2[start]]+=1
                    start+=1

            if(i - start + 1) == n:
                return True
    
        return False
