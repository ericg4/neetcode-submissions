class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 1
        if not nums:
            return 0

        for num in nums:
            if num - 1 not in numSet:
                val = num
                seqLen = 1
                while val + 1 in numSet:
                    seqLen += 1
                    val += 1
                    if seqLen > longest:
                        longest = seqLen
        
        return longest