class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')
        i = j = 0
        currSum = 0

        while j < len(nums):
            currSum += nums[j]
            largest = max(largest, currSum)
            if currSum < 0:
                currSum = 0
            j+=1
        return largest