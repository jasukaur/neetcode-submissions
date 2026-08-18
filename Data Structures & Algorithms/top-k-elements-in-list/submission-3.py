class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        counter = collections.Counter(nums)
        # print(counter)
        for num, times in counter.items():
            freq[times].append(num)

        # print(freq)

        sol = []

        for f in range(len(freq)-1, 0, -1):
            for n in freq[f]:

                sol.append(n)
                if len(sol) == k:
                    return sol
        return []