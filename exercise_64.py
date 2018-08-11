class Solution:
    def sum(self, ilist):
        res = 0
        for element in ilist:
            res = res + element
        return res

    def minSum(self, grid, i, j): # i : rows, j : columns
            for y in range(1, j + 1):
               grid[0][y] = grid[0][y - 1] + grid[0][y]

            for x in range(1, i + 1):
           	   grid[x][0] = grid[x - 1][0] + grid[x][0]

            for x in range(1, i + 1):
                for y in range(1, j + 1):
                   grid[x][y] = grid[x][y] + min(grid[x - 1][y], grid[x][y - 1])

            print("grid : ", grid)

            return grid[i][j]

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        print('m , n : ', m, n)
        return self.minSum(grid, m - 1, n - 1)

def main():
    solution = Solution()
    Grid = [[1, 2, 5], [3, 2, 1]]
    print(solution.minPathSum(Grid))


if __name__ == "__main__":
       main()