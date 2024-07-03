# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # set curr to head
        while curr: # loop through curr
            currNum = curr.val # current number = current value
            currNode = curr # current node = curr
            while curr and curr.val == currNum: # while we have a duplicate
                curr = curr.next
            currNode.next = curr # the next node is the non-duplicate
        return head