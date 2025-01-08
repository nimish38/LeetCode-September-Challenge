from collections import deque

class Solution:
    def slidingPuzzle(self, board) -> int:
        q, curr, target = deque(),"" , "123450"
        swaps = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [3, 5, 1], 5: [4, 2]}
        for _ in range(2):
            curr += ''.join(board[_])
        q.append(curr)
        