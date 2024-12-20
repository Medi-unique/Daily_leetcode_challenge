# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            depth += 1
            if depth & 1:
                n = len(q)
                for i in range(n//2):
                    q[i].val, q[n-1-i].val = q[n-1-i].val, q[i].val
                
        return root