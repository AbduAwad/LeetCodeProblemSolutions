# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        currNode = ListNode()
        head = currNode
        while list1 and list2:
            if list1.val < list2.val:
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next
        currNode.next = list1 or list2
        return head.next
        

            

