class Solution:
    def compress(self, chars) -> int:
        i, j, curr, cnt = 1, 1, chars[0], 1
        while i < len(chars):
            if chars[i] != curr:
                if cnt > 1:
                    for c in str(cnt):
                        chars[j] = c
                        j += 1
                    chars[j] = chars[i]
                    j += 1
                    curr, cnt = chars[i], 1
                j += 1
            else:
                cnt += 1
        return j
    