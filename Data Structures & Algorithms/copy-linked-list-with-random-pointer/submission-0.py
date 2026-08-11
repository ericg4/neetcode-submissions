"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        go through linked list via next nodes
        keep map of nodes to copied nodes O(n) space
        
        """
        if not head:
            return None
        
        nodeMap = {head: Node(head.val), None: None}
        cur = head

        while cur:
            nxt = cur.next
            if nxt not in nodeMap:
                nodeMap[nxt] = Node(nxt.val)
            nodeMap[cur].next = nodeMap[nxt]
            
            rand = cur.random
            if rand not in nodeMap:
                nodeMap[rand] = Node(rand.val)
            nodeMap[cur].random = nodeMap[rand]
            
            cur = cur.next
        
        return nodeMap[head]
            
            
            

