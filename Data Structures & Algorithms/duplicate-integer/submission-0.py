class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for val in nums:
            if val in numSet:
                return True
            numSet.add(val)
        
        return False