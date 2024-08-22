from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordList, que = dict.fromkeys(wordList, 0), deque([beginWord])
        if endWord not in wordList:
            return 0
