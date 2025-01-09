class Solution:
    def findWords(self, board, words):
        res, m, n, tree = [], len(board), len(board[0]), {}

        for word in words:
            curr = tree
            for i in range(len(word)):
                if word[i] not in curr:
                    curr[word[i]] = {}
                curr = curr[word[i]]
            curr['*'] = word
        print(tree)
        return res


print(Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))