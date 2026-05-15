class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for s in asteroids:
            while stack and s < 0 and stack[-1] > 0:
                diff = s + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    s = 0
                else:
                    s = 0
                    stack.pop()
            if s:
                stack.append(s)
        return stack

        