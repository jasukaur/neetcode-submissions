class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones= [-stone for stone in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            if len(self.stones) > 1:
                s1= -heapq.heappop(self.stones)
                s2= -heapq.heappop(self.stones)

                res = abs(s1-s2)
                if res> 0:
                    heapq.heappush(self.stones, -res)
        if self.stones: 
            return -self.stones[0]
        return 0

