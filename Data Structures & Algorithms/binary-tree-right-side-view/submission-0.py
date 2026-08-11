# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)

        res = []
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if len(res) == level:
                    res.append(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            level += 1
        return res