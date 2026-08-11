class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        2, 20, 4, 10, 3, 4, 5
        20, 10, 5

        x.  x.  +1 +1 (3) +1 (4) x
        4 is max
        """
        if not nums:
            return 0

        num_set = set(nums)
        top_set = set()

        for num in num_set:
            if (num + 1) not in num_set:
                top_set.add(num)
        
        max_count = 1
        for num in top_set:
            curr_count = 1
            next_num = num - 1
            while (next_num) in num_set:
                curr_count += 1
                next_num -= 1
            if curr_count > max_count:
                max_count = curr_count
        
        return max_count