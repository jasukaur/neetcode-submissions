class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minN = nums[0]

        while l <=r:
            if nums[l] < nums[r]:
                minN = min(minN, nums[l])
                break

            m = (l+r) //2
            minN = min(minN, nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        return minN

