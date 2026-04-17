class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        pt = 0

        while pt < n:
            target = -nums[pt]
            l, r = pt + 1, n - 1

            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    ans.append([nums[pt], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

            while pt + 1 < n and nums[pt + 1] == nums[pt]:
                pt += 1
            pt += 1

        return ans
