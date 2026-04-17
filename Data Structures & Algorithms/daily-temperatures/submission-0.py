class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = []

        for t in range(len(temperatures)):
            # if stack and temperatures[stack[-1]] < temperatures[t]:
            while stack and temperatures[stack[-1]] < temperatures[t]:
                day = stack.pop()
                result[day] = t-day
            stack.append(t)
        return result
                



