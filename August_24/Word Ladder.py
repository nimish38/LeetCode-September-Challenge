from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordList, que, cnt = dict.fromkeys(wordList, 0), deque([beginWord]), 0
        if endWord not in wordList:
            return 0

        vis, letters = {}, set()
        for w in wordList:
            letters.add(set(w))
        
        while que:
            lvl = len(que)
            for _ in range(lvl):
                word = que.popleft()
                if word == endWord:
                    return cnt
