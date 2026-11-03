class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        check_val = defaultdict(set)
        while(i < len(board)):
            j = 0
            while(j < len(board[0])):
                val = board[i][j]
                if val != ".":
                    if val in check_val[("row", i, val)]:
                        return False
                    else:
                        check_val[("row", i, val)].add(val)
                    if val in check_val[("col", j, val)]:
                        return False
                    else:
                        check_val[("col", j, val)].add(val)
                    if val in check_val[("square", (i//len(board)**0.5, j//len(board)**0.5), val)]:
                        return False
                    else:
                        check_val[("square", (i//len(board)**0.5, j//len(board)**0.5), val)].add(val)
                j+=1
            i+=1
        return True