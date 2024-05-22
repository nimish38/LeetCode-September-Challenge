class Solution:
    def fullJustify(self, words, maxWidth):
        i, res = 0, []
        while i < len(words) :
            lettercount, curr, selectedWords = 0, '', []
            while i < len(words) and lettercount + len(words[i]) < maxWidth:
                lettercount += len(words[i]) + 1
                selectedWords.append(words[i])
                i += 1
            lettercount -= 1
            if len(selectedWords) == 1:
                curr += selectedWords[0] + (' ' * (maxWidth - lettercount))
            else:
                if i == len(words):
                    for k in selectedWords:
                        curr += k + ' '
                    curr += (' ' * (maxWidth - lettercount))
                else:
                    extras = maxWidth - lettercount
                    additional = extras // (len(selectedWords) - 1)
                    left_margin = extras % (len(selectedWords) - 1)

                    curr += selectedWords[0] + ' ' + (' ' * (additional + left_margin))
                    for j in range(1, len(selectedWords) - 1):
                        curr += selectedWords[j] + ' ' + (' ' * additional)
                    curr += selectedWords[-1]
            res.append(curr)

        return res

print(Solution().fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
print(["What   must   be","acknowledgment  ","shall be        "])