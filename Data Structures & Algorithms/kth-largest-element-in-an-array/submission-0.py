class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        newNums = [-n for n in nums]

        heap = heapq.heapify(newNums)

        for i in range(k-1):
            heapq.heappop(newNums)
        
        return -newNums[0]



