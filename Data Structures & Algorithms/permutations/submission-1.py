class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [2,3]
        [1]

        [1,3]
        [2]
        """
        
        res = []

        def backtrack(cur, TODO):
            if not TODO:
                res.append(cur.copy())
                return
            for dig in TODO:
                cur.append(dig)
                copyArr = TODO.copy()
                copyArr.remove(dig)
                backtrack(cur, copyArr)
                cur.pop()
        
        
        backtrack([], nums)
        return res