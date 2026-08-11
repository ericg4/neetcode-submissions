class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        bfs - mark spots as X after visited
        look only for 1s
        """
        islandCount = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != "1":
                    continue
                
                islandCount += 1

                q = [(r, c)]

                while q:
                    newR, newC = q.pop(0)
                    grid[newR][newC] = "X"
                    
                    for dr, dc in directions:
                        tempR = newR + dr
                        tempC = newC + dc
                        if (tempR < 0 or tempC < 0 or 
                            tempR == ROWS or tempC == COLS or 
                            grid[tempR][tempC] != "1"):
                            continue
                        q.append((tempR, tempC))

        return islandCount

                    



                