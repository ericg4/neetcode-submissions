# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if root1 and root2 and root1.val != root2.val:
                return False
            
            if root1 and not root2:
                return False

            if root2 and not root1:
                return False
            
            if not root1 and not root2:
                return True

            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
        
        stack = [root]

        if not subRoot:
            return True

        while stack:
            node = stack.pop()
            if not node:
                continue
            
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    return True

            stack.append(node.left)
            stack.append(node.right)

        return False