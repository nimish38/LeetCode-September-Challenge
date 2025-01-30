class Master:
    def guess(self, word: str) -> int:
        return len(word)


class Solution:
    def findSecretWord(self, words, master) -> None:
        def eleminate(ind, cnt):
            new_list = []
            for j in range(len(words)):
                if j != ind:
                    curr = sum(char1 == char2 for char1, char2 in zip(ind, words[j]))
                    if curr == cnt:
                        new_list.append(words[j])
            return new_list

        def get_best_word():
            cnt = [[0] * 26 for _ in range(6)]
            for w in words:
                for i, c in enumerate(w):
                    cnt[i][ord(c) - ord('a')] += 1

            top_word, best = '', 0
            for w in words:
                curr = 0
                for i, c in enumerate(w):
                    curr += cnt[i][ord(c) - ord('a')]
                if curr > best:
                    best, top_word = curr, w
            return w

        while words:
            val = get_best_word()
            match = master.guess(val)
            if match == 6:
                return
            words = eleminate(val, match)


mas = Master()
Solution().findSecretWord(words=["acckzz","ccbazz","eiowzz","abcczz"], master=mas)