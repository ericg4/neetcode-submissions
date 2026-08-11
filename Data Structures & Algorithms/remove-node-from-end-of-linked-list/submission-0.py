# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = head
        totalLen = 0

        while curr:
            totalLen += 1
            curr = curr.next
        
        numToRemove = totalLen - n

        activeCount = 0

        curr = dummy
        while curr:
            if activeCount == numToRemove:
                curr.next = curr.next.next
                return dummy.next
            curr = curr.next
            activeCount += 1
