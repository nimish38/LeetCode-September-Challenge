class Solution:
    def fullJustify(self, words, maxWidth: int):

        def build_sentence(sent, last):
            cnt, line = len(sent) - 1, ''
            if last:
                for _ in range(cnt):
                    line += sent[_] + ' '
                line += sent[_]
                remaining = maxWidth - len(line)
                line += ' ' * remaining
                return line
            if cnt > 0:


        word, res, minspaces = 0, '', 0
        while word < len(words):
            curr, available = [], maxWidth
            while word < len(words) and available > len(words[word]):
                curr.append(words[word])
                available = available - len(words[word]) - (len(curr) - 1)
                word += 1
            res += build_sentence(curr, word == len(words)) + '\n'
        return res
