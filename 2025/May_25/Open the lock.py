from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        que, cnt, deadends = deque(['0000']), 0, {x : 1 for x in deadends}
        if '0000' in deadends:
            return -1
        def add_neighbors(curr):
            deadends[curr] = 1
            curr = list(curr)
            for i in range(4):
                temp = curr[i]
                curr[i] = '0' if curr[i] == '9' else chr(ord(curr[i]) + 1)
                x = ''.join(curr)
                if x not in deadends:
                    que.append(x)
                    deadends[x] = 1
                curr[i] = temp
                curr[i] = '9' if curr[i] == '0' else chr(ord(curr[i]) - 1)
                x = ''.join(curr)
                if x not in deadends:
                    que.append(x)
                    deadends[x] = 1
                curr[i] = temp

        while que:
            for _ in range(len(que)):
                state = que.popleft()
                if state == target:
                    return cnt
                add_neighbors(state)
            cnt += 1
        return -1

print(Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))