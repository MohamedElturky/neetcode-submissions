class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            freqL = [0] *26
            for letter in word:
                freqL[ord(letter)-97]+=1
            freq = tuple(freqL)
            if freq in words:
                words[freq].append(word)
            else:
                words[freq] = [word]
        
        return list(words.values())
