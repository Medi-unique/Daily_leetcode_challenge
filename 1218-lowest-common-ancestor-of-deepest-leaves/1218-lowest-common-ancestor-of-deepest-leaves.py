
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lca(root):
            if not root:
                return (0, None)
            d_l, l_lca = lca(root.left) 
            d_r, r_lca = lca(root.right) 
            if d_l == d_r:
                return d_r + 1, root

            return (d_r + 1, r_lca) if d_l < d_r else (d_l + 1, l_lca)
        
        return lca(root)[1]