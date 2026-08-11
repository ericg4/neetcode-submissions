# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
                10
            5       15

        """

        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            isLeftValid = dfs(node.left, left, node.val)
            isRightValid = dfs(node.right, node.val, right)

            return isLeftValid and isRightValid
        
        return dfs(root, -101, 101)