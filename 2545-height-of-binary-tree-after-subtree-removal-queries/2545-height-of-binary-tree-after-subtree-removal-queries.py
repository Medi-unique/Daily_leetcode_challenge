# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        n = [0] * ((10**5) + 1)
        d = defaultdict(list)

        def rec(node, deep):
            if not node: return 0
            max_deep = max(rec(node.right, deep+1)+1, rec(node.left, deep+1)+1)

            if len(d[deep]) == 0:
                d[deep].append((max_deep+deep-1, node.val))
            elif len(d[deep]) == 1:
                if max_deep+deep-1 > d[deep][0][0]:
                    d[deep].insert(0, (max_deep+deep-1, node.val))
                else:
                    d[deep].append((max_deep+deep-1, node.val))
            else:
                current = max_deep+deep-1
                if current > d[deep][1][0]:
                    if current > d[deep][0][0]:
                        d[deep][0], d[deep][1] = (current, node.val), d[deep][0]
                    else:
                        d[deep][1] = (current, node.val)
                    
            n[node.val] = deep
            return max_deep
        
            
        rec(root, 0)
        ans = []
        for num in queries:
            if len(d[n[num]]) == 1: 
                ans.append(n[num]-1)
            else:
                ans.append(d[n[num]][0][0] if d[n[num]][0][1] != num else d[n[num]][1][0])
        
        return ans
            
            