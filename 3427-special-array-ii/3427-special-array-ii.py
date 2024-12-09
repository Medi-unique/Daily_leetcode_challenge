class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        special_arrs, prev, parity = [], 0, None
        for i, n in enumerate(nums + [nums[-1]]):
            if n % 2 == parity:
                special_arrs.append((prev, i - 1))
                prev = i
            parity = n % 2
        
        start_idxs, end_idxs = zip(*special_arrs)
        
        res = []
        for a, b in queries:
            s_idx_idx = max(0, bisect.bisect(start_idxs, a) - 1)
            
            e_idx = end_idxs[s_idx_idx] if s_idx_idx < len(end_idxs) else end_idxs[-1]
            
            res.append(e_idx >= b)
            
        return res