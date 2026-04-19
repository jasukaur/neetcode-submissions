class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j =len(nums)-2
        goal = len(nums)-1

        while j > -1:
            if j + nums[j] >= goal:
                goal = j
            j -=1
        
        return goal ==0
