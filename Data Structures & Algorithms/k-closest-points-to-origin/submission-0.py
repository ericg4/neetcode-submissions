class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distSq(point):
            return point[0] * point[0] + point[1] * point[1]
        
        points = [[distSq(pt), pt[0], pt[1]] for pt in points]

        heapq.heapify(points)

        results = []

        for i in range(k):
            val = heapq.heappop(points)
            results.append([val[1], val[2]])
        
        return results