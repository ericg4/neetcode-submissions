class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(rowNum):
            row = [0 for _ in range(9)]

            for i in board[rowNum]:
                if i == ".":
                    continue
                if row[int(i) - 1] == 1:
                    return False
                row[int(i) - 1] = 1
            return True
        
        def isValidCol(colNum):
            col = [0 for _ in range(9)]

            for i in range(9):
                num = board[i][colNum]
                if num == ".":
                    continue
                if col[int(num) - 1] == 1:
                    return False
                col[int(num) - 1] = 1
            
            return True
        
        def isValidSquare(rowNum, colNum):
            xbounds = [rowNum * 3, rowNum * 3 + 3]
            ybounds = [colNum * 3, colNum * 3 + 3]

            nums = [0 for _ in range(9)]

            for i in range(ybounds[0], ybounds[1]):
                for j in range(xbounds[0], xbounds[1]):
                    num = board[i][j]
                    if num == ".":
                        continue
                    num = int(num)
                    if nums[num - 1] == 1:
                        return False
                    nums[num - 1] = 1
            
            return True
        
        for i in range(9):
            validCol = isValidCol(i)
            validRow = isValidRow(i)

            if not validCol or not validRow:
                return False
        
        for i in range(3):
            for j in range(3):
                validSquare = isValidSquare(i, j)

                if not validSquare:
                    return False
        
        return True
        
