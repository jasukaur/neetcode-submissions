class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        ans = []

        for i in range(1, len(nums)):
            left.append(left[-1]* nums[i-1])
        print(left)

        for i in range(len(nums)-2, -1, -1):
            right.append(right[-1]* nums[i+1])
        right.reverse()
        print(right)

        for i in range(len(nums)):
            ans.append(left[i] * right[i])
        return ans
        