# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        #achar o meio
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #inverter a segunda metade
        prev = None
       #None <- 5  3 -> 2 -> None -> None  |   None - > 5 -> 3 -> 2 -> None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        #checando o palindromo
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


