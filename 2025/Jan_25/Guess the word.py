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

        while words:
            val = get_best_word()
            match = master.guess(val)
            if match == 6:
                return
            words = eleminate(val, match)


mas = Master()
Solution().findSecretWord(words=["acckzz","ccbazz","eiowzz","abcczz"], master=mas)