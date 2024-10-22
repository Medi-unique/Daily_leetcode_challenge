# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSum = [root.val]
        currentLevel = [root]
        nxtLevel = []
        if root.left is not None:
            nxtLevel.append(root.left)
        if root.right is not None:
            nxtLevel.append(root.right)


        while len(nxtLevel) != 0:
            currentLevel = nxtLevel[:]
            nxtLevel = []

            for node in currentLevel:
                if node.left is not None:
                    nxtLevel.append(node.left)
                if node.right is not None:
                    nxtLevel.append(node.right)

            levelSum.append(sum([n.val for n in currentLevel]))

        if len(levelSum) < k:
            return -1

        levelSum.sort()
        return levelSum[-k]