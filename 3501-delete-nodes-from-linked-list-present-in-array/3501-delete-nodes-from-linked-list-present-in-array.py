class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums) 
        ans = ListNode(0)
        tail = ans

        while head:
            val = head.val
            head = head.next
            if val not in nums:
                tail.next = ListNode(val)
                tail = tail.next
        return ans.next