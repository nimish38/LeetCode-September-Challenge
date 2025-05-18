class Solution(object):
    def carFleet(self, target, position, speed):
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x:x[0], reverse=True)
        st = []
        for i in range(len(pairs)):
            p, s = pairs[i]
            val = (target - p ) / s
            if not st or val > st[-1]:
                st.append(val)
        return len(st)

print(Solution().carFleet(target = 10, position = [6, 8], speed = [3, 2]))
