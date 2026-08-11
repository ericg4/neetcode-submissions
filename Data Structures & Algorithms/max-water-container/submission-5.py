class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        1, 7, 2, 5, 4, 7, 3, 6
        l                    r
        """

        l_ptr = 0
        r_ptr = len(heights) - 1

        max_vol = 0

        while (l_ptr < r_ptr):
            l_height = heights[l_ptr]
            r_height = heights[r_ptr]

            curr_vol = min(l_height, r_height) * (r_ptr - l_ptr)

            if curr_vol > max_vol:
                max_vol = curr_vol
            
            if l_height < r_height:
                l_ptr += 1
            else:
                r_ptr -= 1
        
        return max_vol