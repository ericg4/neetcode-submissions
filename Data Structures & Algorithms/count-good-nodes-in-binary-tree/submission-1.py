# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            
            newMax = max(maxVal, node.val)
            
            res += dfs(node.left, newMax)
            res += dfs(node.right, newMax)

            return res
        
        return dfs(root, root.val)