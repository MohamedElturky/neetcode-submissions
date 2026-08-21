class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        n = len(temperatures)
        answer = [0] * n

        for i in range(1, n):
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                value, index = stack.pop()
                answer[index] = i - index
            
            stack.append((temperatures[i], i))

        return answer
            

