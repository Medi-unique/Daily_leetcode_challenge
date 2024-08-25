class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root: Optional[TreeNode]) -> List[int]:
            if root:
                preorder(root.left)
                preorder(root.right)
                result.append(root.val)
            return result
        return preorder(root)