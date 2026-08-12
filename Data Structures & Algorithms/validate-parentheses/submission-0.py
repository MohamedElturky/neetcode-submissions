class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            elif (bracket == ')' or bracket == '}' or bracket == ']') and stack:
                if (bracket == ')' and stack[-1] == '(') or (bracket == '}' and stack[-1] == '{') or (bracket == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if not stack:
            return True
        else:
            return False            
                