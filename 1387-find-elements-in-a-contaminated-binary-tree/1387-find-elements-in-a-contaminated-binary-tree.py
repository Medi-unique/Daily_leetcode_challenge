class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        self.solve(root, 0)

    def solve(self, node, val):
        if not node:
            return
        node.val = val
        self.values.add(val)
        self.solve(node.left, 2 * val + 1)
        self.solve(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values