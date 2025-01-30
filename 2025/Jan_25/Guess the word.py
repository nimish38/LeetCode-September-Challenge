class Master:
    def guess(self, word: str) -> int:
        return len(word)


class Solution:
    def findSecretWord(self, words, master) -> None:
        for word in words:
            print(master.guess(word))


mas = Master()
Solution().findSecretWord(words=["acckzz","ccbazz","eiowzz","abcczz"], master=mas)