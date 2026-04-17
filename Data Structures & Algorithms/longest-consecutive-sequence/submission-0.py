class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxL = 0

        starts= []

        for n in nums:
            if n-1 not in s:
                print(n)
                starts.append(n)
        
        
        for i in starts:
            currL= 1
            while i +1 in s:
                currL +=1
                i+=1
            
            maxL= max(maxL, currL)
        return maxL
