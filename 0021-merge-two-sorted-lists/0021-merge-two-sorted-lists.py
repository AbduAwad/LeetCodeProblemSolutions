# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        currNode = ListNode()
        temp = currNode
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                currNode.next = list1
                list1 = list1.next
            else: 
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next

        if list1 == None:
            currNode.next = list2
        else:
            currNode.next = list1
        return temp.next