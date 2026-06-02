class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starter = []
        numsSet = set(nums)

        for n in nums:
            if n-1 not in nums:
                starter.append(n)
        
        maxLength = 0

        for s in starter:
            currL = 0
            while s in numsSet:
                currL += 1
                maxLength = max(maxLength, currL)
                s += 1
        
        return maxLength
