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

print(Solution().fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))
print(["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "])