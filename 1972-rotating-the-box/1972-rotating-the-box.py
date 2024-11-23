class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        ans = list(box)

        for i, row in enumerate(box):
            start = 0
            for j, value in enumerate(row):
                if value != '#':
                    start = j + 1
                else:
                    if j + 1 < cols and box[i][j + 1] == '.':
                        ans[i][start], ans[i][j + 1] = '.', '#'
                        start += 1

        return [[ans[i][j] for i in range(rows - 1, -1, -1)] for j in range(cols)]