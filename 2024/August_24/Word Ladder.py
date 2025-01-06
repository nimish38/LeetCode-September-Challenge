from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordList, que, cnt = dict.fromkeys(wordList, 0), deque([beginWord]), 0
        if endWord not in wordList:
            return 0

        vis, letters, n = {}, set(), len(beginWord)
        for w in wordList:
            letters = letters.union(set(w))

        while que:
            lvl = len(que)
            for _ in range(lvl):
                word = que.popleft()
                if word == endWord:
                    return cnt
                for i in range(n):
                    for char in letters:
                        new_word = word[:i] + char + word[i + 1:]
                        if new_word not in vis and new_word in wordList and new_word not in que:
                            que.append(new_word)
                            vis[word] = 1
            cnt += 1
        return 0

print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))