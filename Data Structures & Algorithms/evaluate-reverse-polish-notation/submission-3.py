class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for token in tokens:
            if token == "+":
                first = values.pop()
                second = values.pop()
                answer = first + second
                values.append(answer)

            elif token == "-":
                first = values.pop()
                second = values.pop()
                answer = second - first
                values.append(answer)

            elif token == "*":
                first = values.pop()
                second = values.pop()
                answer = first * second
                values.append(answer)

            elif token == "/":
                first = values.pop()
                second = values.pop()
                answer = second / first
                values.append(int(answer))

            else:
                values.append(int(token)) 
        
        return values[0]