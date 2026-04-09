class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x, y = points[i]
            distance = (x**2) + (y**2)
            minHeap.append([distance, x, y])
            
        heapq.heapify(minHeap)
        res = []
        while 0 < k:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res