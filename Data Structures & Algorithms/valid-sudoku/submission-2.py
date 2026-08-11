class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        box_sets = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                
                # Check row set:
                if value in row_sets[i]:
                    print(value, "row", i, row_sets[i])
                    return False
                row_sets[i].add(value)

                # Check col set:
                if value in col_sets[j]:
                    print(value, "col", j, col_sets[j])
                    return False
                col_sets[j].add(value)

                # Check box set:
                box_id = (i // 3) * 3 + (j // 3)
                if value in box_sets[box_id]:
                    print(value, "box", box_id, box_sets[box_id])
                    return False
                box_sets[box_id].add(value)
        
        return True