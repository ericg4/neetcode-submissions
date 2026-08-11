class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1,5,2,3,4
        0,5,5,5,5
        5,4,4,4,0
        """
        if not height:
            return 0
        
        lp = 0
        rp = len(height) - 1

        lMax = height[lp]
        rMax = height[rp]

        water = 0

        while lp < rp:
            if lMax < rMax:
                lp += 1
                lMax = max(lMax, height[lp])
                water += lMax - height[lp]
            else:
                rp -= 1
                rMax = max(rMax, height[rp])
                water += rMax - height[rp]
        return water