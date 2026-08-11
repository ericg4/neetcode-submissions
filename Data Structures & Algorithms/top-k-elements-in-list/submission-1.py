class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,2,3,3,3]
        """

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, val in count.items():
            freq[val].append(key)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
        