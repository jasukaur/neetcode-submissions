class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm:
                if abs(i- hm[nums[i]]) <= k:
                    # print(i, nums[i])
                    return True
                else:
                    hm[nums[i]] = i
            else:
                hm[nums[i]] = i
            # print(hm)
        return False
