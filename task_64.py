from typing import List


class Task64:

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)

        line_0 = grid[0]
        n = len(line_0)
        array = [0] * n

        s = 0
        for i in range(0, n):
            s += line_0[i]
            array[i] = s

        for j in range(1, m):
            line = grid[j]
            s = array[0] + line[0]
            array[0] = s
            for i in range(1, n):
                sa = array[i]
                if s > sa:
                    s = sa
                s += line[i]
                array[i] = s

        return array[n - 1]
