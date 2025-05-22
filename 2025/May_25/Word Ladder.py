from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList, que, level, vis, chars = set(wordList), deque([beginWord]), 1, set(), set()
        if endWord not in wordList:
            return 0
        for word in wordList:
            for c in word:
                chars.add(c)

        def explore(word):
            word = list(word)
            for i in range(len(word)):
                t = word[i]
                for c in chars:
                    word[i] = c
                    new_word = ''.join(word)
                    if new_word not in vis and new_word in wordList:
                        que.append(new_word)
                        vis.add(new_word)
                word[i] = t

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node == endWord:
                    return level
                explore(node)
            level += 1
        return 0

print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))