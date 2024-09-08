class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.countNodes(head)
        parts, r = divmod(n, k)
        res = [None] * k
        curr = head
        for i in range(k):
            res[i] = curr
            for j in range(parts + (r > 0) - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            r -= 1
        return res

    def countNodes(self, head: ListNode) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count