class Solution:
    def fullJustify(self, words, maxWidth: int):

        def build_sentence(sent, last, txt):
            cnt, line = len(sent) - 1, ''
            if last:
                _ = 0
                for _ in range(cnt):
                    line += sent[_] + ' '
                line += sent[_]
                remaining = maxWidth - len(line)
                line += ' ' * remaining
            else:
                if cnt > 0:
                    extra = maxWidth - txt - cnt
                    pad = extra // cnt
                    left_pad = extra % cnt
                    for i in range(cnt):
                        line += sent[i] + ' ' + (' ' * pad)
                        if left_pad > 0:
                            line += ' '
                            left_pad -= 1
                    line += sent[i + 1]
                else:
                    line += sent[0] + ' ' * (maxWidth - txt)
            return line

        word, res, minspaces = 0, [], 0
        while word < len(words):
            curr, available = [], maxWidth
            while word < len(words) and available - (len(curr) - 1) >= len(words[word]):
                curr.append(words[word])
                available = available - len(words[word])
                word += 1
            res.append(build_sentence(curr, word == len(words), maxWidth - available))
        return res


print(Solution().fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))