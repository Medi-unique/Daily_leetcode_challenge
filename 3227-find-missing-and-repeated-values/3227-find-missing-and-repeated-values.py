class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n_sq = n ** 2
        all_nums = set(range(1, n_sq + 1))

        def idx_to_coords(i: int) -> tuple[int]:
            return i // n, i % n

        def recurse(idx: int, repeated: int, missing: int, seen: set[int]):
            if idx == -1:
                return repeated, (all_nums ^ seen).pop()

            i, j = idx_to_coords(idx)
 
            if grid[i][j] in seen:
                r, m = recurse(idx - 1, grid[i][j], missing, seen)
                if r != -1 and m != -1:
                    return r, m
            else:
                r, m = recurse(idx - 1, repeated, missing, seen | {grid[i][j]})
                if r != -1 and m != -1:
                    return r, m

            return r, m

        return recurse(n_sq - 1, -1, -1, set())