"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        bfs through whole thing

        rebuild one step at a time
        keep map of nodes to copies so that we have full access to 
        all neighbor nodes whenever we want
        """
        if not node:
            return None
        
        nodeMap = {node: Node(node.val)}
        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if nei not in nodeMap:
                    nodeMap[nei] = Node(nei.val)
                    q.append(nei)
                nodeMap[cur].neighbors.append(nodeMap[nei])
        
        return nodeMap[node]

