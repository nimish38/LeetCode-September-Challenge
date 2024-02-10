class Solution:
    def compress(self, chars):
        if len(chars):
            cnt, prevChar, changed = 1, chars[0], 0
            for i in range(1, len(chars)):
                if chars[i] != prevChar:
                    chars[changed] = prevChar
                    prevChar = chars[i]
                    changed += 1
                    if cnt > 1:
                        chars[changed] = cnt
                        changed += 1
                        cnt = 1
                else:
                    cnt += 1
            if cnt > 1:
                chars[changed] = prevChar
                changed += 1
                chars[changed] = cnt
                print(chars[:changed + 1])
                return changed + 1
            return 1

a = Solution()
print(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))