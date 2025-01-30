class Master:
    def guess(self, word: str) -> int:
        return len(word)


class Solution:
    def findSecretWord(self, words, master) -> None:
        def eleminate(ind, cnt):
            j = 0
            while j < len(words):
                if j != ind:
                    curr = 0
                    for x in range(6):
                        if words[ind] == words[j]:
                            curr += 1
                    if curr != cnt:
                        del words[j]
                    else:
                        j += 1
        i = 0
        while words:
            val = words[i]
            match = master.guess(val)
            if match == 6:
                return
            eleminate(i, match)
            i += 1


mas = Master()
Solution().findSecretWord(words=["acckzz","ccbazz","eiowzz","abcczz"], master=mas)