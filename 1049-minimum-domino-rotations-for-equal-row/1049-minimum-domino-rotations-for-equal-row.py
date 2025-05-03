class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        first = tops[0]
        second = bottoms[0]

        top_first = 0
        top_second = 1
        bottom_first = 1
        bottom_second = 0

        first_can = True
        second_can = True

        for i in range(1, len(tops)):
            top = tops[i]
            bottom = bottoms[i]

            if top != first and bottom != first:
                first_can = False
            if top != second and bottom != second:
                second_can = False
            if top == bottom:
                continue
            if bottom == first:
                top_first += 1
            if bottom == second:
                top_second += 1
            if top == second:
                bottom_second += 1
            if top == first:
                bottom_first += 1
        if not first_can and not second_can:
            return -1
        elif not second_can:
            return min(top_first, bottom_first)
        elif not first_can:
            return min(top_second, bottom_second)
        else:
            return min([top_first, bottom_first, top_second, bottom_second])