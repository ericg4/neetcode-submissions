# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        temp1 = root.left
        temp2 = root.right
        root.left = self.invertTree(temp2)
        root.right = self.invertTree(temp1)

        return root