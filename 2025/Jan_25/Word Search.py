class Solution:
    def findWords(self, board, words):
        res, m, n, tree = [], len(board), len(board[0]), {}

        def getWords(i, j, root):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            letter = board[i][j]
            if letter in root:
                if '*' in root[letter]:
                    res.append(root[letter]['*'])

                board[i][j] = '#'
                adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for a, b in adj:
                    getWords(i + a, j + b, root[letter])
                board[i][j] = letter

        for word in words:
            curr = tree
            for i in range(len(word)):
                if word[i] not in curr:
                    curr[word[i]] = {}
                curr = curr[word[i]]
            curr['*'] = word

        for i in range(m):
            for j in range(n):
                if board[i][j] in tree:
                    getWords(i, j, tree)
        return list(set(res))


print(Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))