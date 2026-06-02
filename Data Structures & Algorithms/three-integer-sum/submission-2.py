class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        i = 0
        result = []

        while i < len(nums):
            if i>0 and nums[i] == nums[i-1]:
                i += 1
                continue
            first = nums[i]

            l, r = i+1, len(nums)-1

            while l < r: 
                if first + nums[l] + nums[r] == 0:
                    result.append([first,nums[l],nums[r]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif first + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l +=1
            i +=1
            
        return result

            
        