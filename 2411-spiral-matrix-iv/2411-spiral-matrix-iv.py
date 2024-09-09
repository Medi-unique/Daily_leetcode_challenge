# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]
        current = head
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right and current:
            for i in range(left, right + 1):
                result[top][i] = current.val
                current = current.next
                if not current:
                    return result
            top += 1

            for i in range(top, bottom + 1):
                result[i][right] = current.val
                current = current.next
                if not current:
                    return result
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result[bottom][i] = current.val
                    current = current.next
                    if not current:
                        return result
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result[i][left] = current.val
                    current = current.next
                    if not current:
                        return result
                left += 1
        
        return result