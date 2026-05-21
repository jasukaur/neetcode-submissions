class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)

        freq = [[] for i in range(len(nums)+1)]

        for val, count in count.items():
            freq[count].append(val)

        res = []

        for i in range(len(freq)-1, -1, -1):
            for it in freq[i]:
                if k > 0:
                    res.append(it)
                    k -= 1
        return res

