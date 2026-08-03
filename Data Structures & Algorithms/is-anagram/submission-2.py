class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterS = sorted(s)
        letterT = sorted(t)
        if len(s) != len(t):
            return False
        
        if letterS != letterT:
            return False

        return True