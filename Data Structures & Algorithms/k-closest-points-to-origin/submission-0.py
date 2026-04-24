class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        res = []
        for x,y in points:
            dis = (x **2) + (y**2)
            hp.append([dis, x, y])

        heapq.heapify(hp)

        while k>0:
           dis, x, y = heapq.heappop(hp)
           res.append([x,y])
           k-=1
        return res
