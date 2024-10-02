class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        check=sorted(set(arr))
        count={check[i]:i+1 for i in range(len(check))}
        ans=[]
        for val in arr:
            ans.append(count[val])
        return ans
        