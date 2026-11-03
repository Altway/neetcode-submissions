import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        check_val = set()
        boundary = math.isqrt(len(board))
        while(i < len(board)):
            j = 0
            while(j < len(board[0])):
                val = board[i][j]
                if val != ".":
                    if ("row", i, val) in check_val:
                        return False
                    check_val.add(("row", i, val))
                    if ("col", j, val) in check_val:
                        return False
                    check_val.add(("col", j, val))
                    if ("square", (i//boundary, j//boundary), val) in check_val:
                        return False
                    check_val.add(("square", (i//boundary, j//boundary), val))
                j+=1
            i+=1
        return True