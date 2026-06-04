class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for b in s:
            if b not in brackets:
                stack.append(b)
            else:
                if not stack:
                    return False
                elif stack[-1] != brackets[b]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True
                    
                