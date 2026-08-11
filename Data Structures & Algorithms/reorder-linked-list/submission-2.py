# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0 1 2 3 4 5 6 7
        0 7 1 6 2 5 3 4
        0.  1.  2.  3
          7.  6.  5.  4
        
        0 1 2 3 4 5 6
        0 6 1 5 2 4 3
        0.  1.  2.  
          6.  5.  4 3
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next

        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        firstHead = head
        secondHead = prev

        while firstHead and secondHead:
            temp1 = firstHead.next
            temp2 = secondHead.next
            firstHead.next = secondHead
            secondHead.next = temp1

            firstHead = temp1
            secondHead = temp2
