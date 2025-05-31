from collections import deque
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        st, n, farthest = deque([0]), len(s), 0
        while st:
            ind = st.popleft()
            for i in range(max(ind + minJump, farthest + 1), min(ind + maxJump + 1, n)):
                if s[i] == '0':
                    if i == n - 1:
                        return True
                    st.append(i)
            farthest = ind + maxJump
        return False

print(Solution().canReach(s = "011010", minJump = 2, maxJump = 3))