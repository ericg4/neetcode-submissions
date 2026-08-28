# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverseNode(node, maxVal):
            if not node:
                return 0
            numGood = 0
            newMaxVal = maxVal
            if node.val >= maxVal:
                numGood += 1
                newMaxVal = node.val
            
            leftGood = traverseNode(node.left, newMaxVal)
            rightGood = traverseNode(node.right, newMaxVal)
            numGood += leftGood + rightGood
            return numGood
        
        return traverseNode(root, float('-inf'))