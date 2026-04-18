class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1, 2
        if  n ==1:
            return 1

        for i in range(3, n+1):
            curr = one+two
            one = two
            two = curr
        return two