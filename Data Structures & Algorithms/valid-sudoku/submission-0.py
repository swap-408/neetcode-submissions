class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = [[False]*10 for i in range(0,10)]
        seenCol = [[False]*10 for i in range(0,10)]
        seenBox = [[False]*10 for i in range(0,10)]

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.' : continue
                v = int(board[i][j])
                boxIdx = 3 * (i // 3) + (j // 3)
                cond = seenRow[v][i] or seenCol[v][j] or seenBox[v][boxIdx]
                if cond == True:
                    return False
                seenRow[v][i] = True
                seenCol[v][j] = True
                seenBox[v][boxIdx] = True
        return True