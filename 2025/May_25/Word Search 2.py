class Solution(object):
    def findWords(self, board, words):
        trie, m, n, res = {}, len(board), len(board[0]), []
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = word

        def solve(i, j, curr):
            if '*' in curr:
                res.append(curr['*'])
            temp, board[i][j] = board[i][j], '#'
            for x, y in [(0, 1) ,(0, -1), (1, 0), (-1, 0)]:
                a, b = i + x, j + y
                if 0 <= a < m and 0 <= b < n and board[a][b] in curr:
                    solve(a, b, curr[board[a][b]])
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    solve(i, j, trie[board[i][j]])
        return res

print(Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))