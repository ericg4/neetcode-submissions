class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,2,3,3,3]
        """

        buckets = [[] for _ in range(len(nums) + 1)]

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        
        for i in range(len(buckets) - 1, -1, -1):
            while buckets[i] and k > 0:
                res.append(buckets[i].pop())
                k -= 1
            
        return res