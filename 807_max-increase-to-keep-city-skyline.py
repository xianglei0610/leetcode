#coding=utf-8

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hang = []
        lie = []
        for i in grid:
            hang.append(max(i))
        for j in range(len(grid)):
            lie.append(max([i[j] for i in grid]))

        new_grid = []
        for i in range(len(hang)):
            new_col = []
            for j in range(len(lie)):
                new_col.append(min(hang[i], lie[j]))
            new_grid.append(new_col)
        sum1 = 0
        sum2 = 0
        for i in grid:
            for j in i:
                sum1 += j

        for i in new_grid:
            for j in i:
                sum2 += j
        return sum2-sum1


# grid = [[3,0,8,4],
#         [2,4,5,7],
#         [9,2,6,3],
#         [0,3,1,0]]
# s =Solution()
# s.maxIncreaseKeepingSkyline(grid)