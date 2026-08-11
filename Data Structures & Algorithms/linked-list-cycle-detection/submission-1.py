# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow:
            if fast:
                fast = fast.next
                if fast == slow:
                    return True
                if not fast:
                    return False
                fast = fast.next
            else:
                return False
            slow = slow.next
        return False