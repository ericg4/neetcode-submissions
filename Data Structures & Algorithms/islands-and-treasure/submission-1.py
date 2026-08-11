class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        bfs from each chest, 4 directions (up down left right)
        fill in the values

        """
        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        # get set of all chest locations
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        
        
        curDist = 0
        while q:
            curLen = len(q)

            for i in range(curLen):
                coord = q.popleft()

                r = coord[0]
                c = coord[1]

                # if is shorter path, then set 
                # its new shortest distance and append the new points
                # to traverse
                if grid[r][c] >= 0:
                    if curDist < grid[r][c]:
                        grid[r][c] = curDist
            
                for change in directions:
                    dr = change[0]
                    dc = change[1]
                    newR = r + dr
                    newC = c + dc
                    if (newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or 
                        grid[newR][newC] <= 0 or 
                        (newR, newC) in visited):
                        continue
                    q.append((newR, newC))
                    visited.add((newR, newC))
            
            curDist += 1
        
