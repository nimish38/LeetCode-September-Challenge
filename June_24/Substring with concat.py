class Solution:
    def findSubstring(self, s: str, words):
        word_len, num_words = len(words[0]), len(words)
        n, cnt, res = num_words * word_len, {}, []

        for word in words:
            if word in cnt:
                cnt[word] += 1
            else:
                cnt[word] = 1

        for i in range(0, len(s) - n + 1):
            checklist = dict(cnt)
            for j in range(i, i + n + 1, word_len):
                curr = s[j: j + word_len]
                if curr in checklist:
                    if checklist[curr] == 1:
                        del checklist[curr]
                    else:
                        checklist[curr] -= 1
                else:
                    break
            if len(checklist) == 0:
                res.append(i)
        return res

print(Solution().findSubstring(s = "barfoothefoobar", words = ["foo","bar"]))