class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-s for s in stones]
        heapq.heapify(st)
        print(st)

        while len(st) > 1:
            s1 = -heapq.heappop(st)
            s2 = -heapq.heappop(st)
            if s1 == s2:
                continue
            else:
                heapq.heappush(st, -abs(s1-s2))
                print(st)
        
        if st:
            return -st[0]
        return 0
