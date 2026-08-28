# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverseNode(node):
            if not node:
                return 0
            leftHeight = traverseNode(node.left)
            rightHeight = traverseNode(node.right)

            return max(leftHeight, rightHeight) + 1
        
        return traverseNode(root)