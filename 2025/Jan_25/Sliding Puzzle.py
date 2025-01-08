from collections import deque


class Solution:
    def slidingPuzzle(self, board) -> int:
        def zero_ind(str):
            for i in range(6):
                if str[i] == '0':
                    return i

        q, curr, target = deque(),"" , "123450"
        swaps, cnt, vis = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [3, 5, 1], 5: [4, 2]}, 0, {}
        for _ in range(2):
            for j in range(3):
                curr += str(board[_][j])
        q.append(curr)
        vis[curr] = True

        while q:
            for _ in range(len(q)):
                val = q.popleft()
                if val == target:
                    return cnt
                ind = zero_ind(val)

                for adj in swaps[ind]:
                    state = list(val)
                    state[ind], state[adj] = state[adj], state[ind]
                    state = ''.join(state)
                    if state not in vis:
                        q.append(state)
                        vis[state] = True
            cnt += 1
        return -1


print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))