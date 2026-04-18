class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n * (n+1))//2
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
        return s- curr
