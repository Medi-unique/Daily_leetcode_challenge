# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root,level):
            if root:
                if len(ans) > level:
                    if root.val > ans[level]:
                        ans[level] = root.val
                else:
                    ans.append(root.val)
                traverse(root.left, level + 1)
                traverse(root.right, level + 1)
        traverse(root, 0)
        return ans
