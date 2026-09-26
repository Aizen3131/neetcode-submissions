class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            lis = []
            for y in x:
                if y != "." and y in lis:
                    return False
                else:
                    lis.append(y)

        for w in range(len(board)):
            lis = []
            for z in range(len(board)):
                plac = board[z][w]
                if plac != "." and plac in lis:
                    return False
                else:
                    lis.append(plac)

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                lis = []
                for i in range(3):
                    for j in range(3):
                        plac = board[r + i][c + j]
                        if plac != "." and plac in lis:
                            return False
                        else:
                            lis.append(plac)

        return True