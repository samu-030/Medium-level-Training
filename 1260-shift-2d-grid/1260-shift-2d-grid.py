class Solution(object):
    def shiftGrid(self, grid, k):

        n = len(grid)
        m = len(grid[0])

        total = n * m
        k %= total

        if k == 0:
            return grid

        def reverse_k_vals(l, r):

            while l < r:

                r1 = l // m
                c1 = l % m

                r2 = r // m
                c2 = r % m

                grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

                l += 1
                r -= 1

        reverse_k_vals(0, total -1)
        reverse_k_vals(0, k - 1)
        reverse_k_vals(k, total - 1)

        return grid
        