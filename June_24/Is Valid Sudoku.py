class Solution:
    def isValidSudoku(self, board):
        for row in board:
            num = 0
            curr = set()
            for ele in  row:
                if ele != '.':
                    num += 1
                    curr.add(ele)
            if num != len(curr):
                return False

        for i in range(9):
            num = 0
            curr = set()
            for j in range(9):
                if board[j][i] != '.':
                    num += 1
                    curr.add(ele)
            if num != len(curr):
                return False

            