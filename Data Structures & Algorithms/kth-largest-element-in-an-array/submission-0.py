class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)

        val = 0
        for i in range(k):
            val = heapq.heappop(maxHeap)
        
        return -val