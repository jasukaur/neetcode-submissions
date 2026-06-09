class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        curr = 0

        for n in nums:
            curr += n
            largest = max(largest, curr)

            if curr < 0:
                curr = 0
        return largest
