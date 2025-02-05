from collections import deque


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        st, res = deque((row, column)), 0
        while k > 0 and st:
            curr = 0
            moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
            for _ in range(len(st)):
                a, b = st.popleft()
                for x, y in moves:
                    if 0 <= a + x < n and 0 <= b + y < n:
                        st.append((a + x), (b + y))
                        curr += 1
            res *= (curr / 8)
            k -= 1
        return res