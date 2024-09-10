# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self,num1,num2):
        if (num2 == 0): return num1
        return self.gcd(num2, num1%num2)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while(head.next):
            num1,num2 = head.val, head.next.val
            newNode = ListNode(self.gcd(num1,num2))
            newNode.next = head.next
            head.next = newNode
            head = newNode.next
        return dummy
        