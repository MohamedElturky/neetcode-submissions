class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        freq = {}
        max_freq = 0
        longest = 0

        for c in s:
            if c in freq:
                freq[c]+=1
            else:
                freq[c] = 1
            max_freq = max(max_freq, freq[c])

            window_length = end - start + 1
            rest = window_length - max_freq
            
            if rest > k:
                freq[s[start]]-=1
                start+=1
            
            longest = max(longest, end - start + 1)
            end+=1
        
        return longest

