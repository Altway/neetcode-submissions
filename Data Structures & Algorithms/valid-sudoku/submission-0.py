class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        while(i < len(board)):
            j = 0
            while(j < len(board[0])):
                val = board[i][j]
                if val != ".":
                    if val in row[i]:
                        #print(f" {val} in row at {(i,j)}")
                        return False
                    else:
                        row[i].add(val)
                    if val in col[j]:
                        #print(f" {val} in col at {(i,j)}")
                        return False
                    else:
                        col[j].add(val)
                    if val in square[(i//3, j//3)]:
                        #print(f" {val} in square at {(i,j)}")
                        return False
                    else:
                        square[(i//3, j//3)].add(val)
                j+=1
            i+=1
        #print(f"row {row}")
        #print(f"col {col}")
        #print(f"square {square}")
        return True