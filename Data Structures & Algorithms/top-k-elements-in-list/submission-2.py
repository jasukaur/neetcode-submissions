class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = [[] for _ in range(len(nums) + 1)]

        count_nums = collections.Counter(nums)
        print(count_nums)
        for key,val in count_nums.items():
            ct[val].append(key)
        print(ct)
        
        res = []

        for i in range(len(ct)-1, 0, -1):
            for num in ct[i]:
                res.append(num)
                if len(res) == k:
                    return res
 