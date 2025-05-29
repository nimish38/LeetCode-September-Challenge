class Solution(object):
    def findWords(self, board, words):
        m, n, trie, res = len(board), len(board[0]), {}, []
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
                curr.pop('*')

            temp, board[i][j] = board[i][j], '#'
            for a, b in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#' and board[x][y] in curr:
                    solve(x, y, curr[board[x][y]])
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    solve(i, j, trie[board[i][j]])
        return list(res)

print(Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))