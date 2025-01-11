class Solution:
    def fullJustify(self, words, maxWidth: int):
        word, res, minspaces = 0, '', 0
        while word < len(words):
            curr, available = [], maxWidth
            while available > len(words[word]):
                curr.append(words[word])
                available = available - len(words[word]) - (len(curr) - 1)
                word += 1
            build_sentence(curr)
        return res
