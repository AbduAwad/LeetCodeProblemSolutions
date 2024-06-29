# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        sumStr1, sumStr2 = '',''
        while l1:
            sumStr1 += str(l1.val)
            l1 = l1.next
        while l2:
            sumStr2 += str(l2.val)
            l2 = l2.next
        
        sumStr = str(int(sumStr1) + int(sumStr2))
        temp = node = ListNode()
        for i in range(len(sumStr)):
            if (node):
                node.val = int(sumStr[i])
                if (i < len(sumStr)-1):
                    node.next = ListNode()
                    node = node.next
        return self.reverse(temp)
        
    
    def reverse(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = l1, None
        while curr: # reverse the sll
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev