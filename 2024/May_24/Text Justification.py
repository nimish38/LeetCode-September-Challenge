class Solution:
    def fullJustify(self, words, maxWidth):
        i, res = 0, []
        while i < len(words) :
            lettercount, curr, selectedWords = 0, '', []
            while i < len(words) and lettercount + len(words[i]) <= maxWidth:
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
                    curr += (' ' * (maxWidth - lettercount - 1))
                    curr = curr[:maxWidth]
                else:
                    lettercount -= len(selectedWords) - 1
                    extras = maxWidth - lettercount
                    additional = extras // (len(selectedWords) - 1)
                    left_margin = extras % (len(selectedWords) - 1)

                    for j in range(0, len(selectedWords) - 1):
                        curr += selectedWords[j] + (' ' * additional)
                        if j < left_margin:
                            curr += ' '
                    curr += selectedWords[-1]
            res.append(curr)

        return res

print(Solution().fullJustify(words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], maxWidth = 16))
print(["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"])