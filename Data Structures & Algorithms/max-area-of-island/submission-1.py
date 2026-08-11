class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        bfs - mark spots as X after visited
        look only for 1s
        """
        maxIslandArea = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 1:
                    continue

                q = [(r, c)]
                grid[r][c] = -1
                islandArea = 0
                while q:
                    newR, newC = q.pop(0)
                    print(newR, newC)
                    islandArea += 1
                    
                    for dr, dc in directions:
                        tempR = newR + dr
                        tempC = newC + dc
                        if (tempR < 0 or tempC < 0 or 
                            tempR == ROWS or tempC == COLS or 
                            grid[tempR][tempC] != 1):
                            continue
                        q.append((tempR, tempC))
                        grid[tempR][tempC] = -1

                
                if islandArea > maxIslandArea:
                    maxIslandArea = islandArea

        return maxIslandArea
