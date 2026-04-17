class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        hm = {'}': '{', ']':'[', ')':'('}

        for i in s:
            if i not in hm:
                stack.append(i)
            elif stack:
                if stack[-1] != hm[i]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        
        if len(stack):
            return False
        return True

