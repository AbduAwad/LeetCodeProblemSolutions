# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr: # Determine size of sll
            size += 1
            curr = curr.next
        if (size == n): # If we are removing the first item
            head = head.next
            return head
        count = 1
        curr = head
        while curr: # If we are removing any item other than the first
            if (count == size - n):
                nextNode = curr.next.next
                curr.next = nextNode
                return head
            curr = curr.next
            count += 1