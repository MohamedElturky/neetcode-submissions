class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        n = len(strs)
        encoded += str(n)
        encoded += "."
    
        for word in strs:
            encoded += str(len(word))
            encoded += "."

        for word in strs:
            encoded += word
        
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        n = ""
        while s[i] != ".":
            n += s[i]
            i+=1

        length = int(n)
        nums = [0] * length
        num = ""
        j = 0
        while length > 0:
            i+=1
            if s[i] == ".":
                length-=1
                nums[j] = int(num)
                num = ""
                j+=1
            else:
                num += s[i]
        
        i+=1
        answer = []
        for value in nums:
            word = ""
            while value > 0:
                word += s[i]
                i+=1
                value-=1
            answer.append(word)
        
        return answer



