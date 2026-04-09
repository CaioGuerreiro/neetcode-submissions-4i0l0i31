# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # time O(n)  space O(n)
        # seen = set()
        # cur = head

        # while cur:
        #     if cur in seen:
        #         return True
        #     seen.add(cur)
        #     cur = cur.next

        # return False
        
        # time O(n) space O(1)
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
