class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            '(':')',
            '{':'}',
            '[':']'
        }
        opening = parenthesis.keys()
        closing = parenthesis.values()
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if parenthesis[top] != char:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
