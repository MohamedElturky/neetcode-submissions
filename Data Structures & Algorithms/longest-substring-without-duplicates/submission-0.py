class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        length = 0
        if len(s) == 0:
            return 0

        for c in s:
            if c in seen:
                length = max(length, len(seen))
                while c in seen:
                    seen.remove(s[start])
                    start+=1
                seen.add(c)
            else:
                seen.add(c)
        
        length = max(length, len(seen))
        return length
                
                