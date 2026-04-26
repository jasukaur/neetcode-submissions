class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # i, j = 0, k-1
        # res = []

        # while j < len(nums):
        #     res.append(max(nums[i:j+1]))
        #     i+=1
        #     j+=1
        # return res

        heap, res = [], []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res