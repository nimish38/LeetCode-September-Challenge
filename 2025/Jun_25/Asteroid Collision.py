class Solution(object):
    def asteroidCollision(self, asteroids):
        st = []
        for ast in asteroids:
            if not st or ast > 0:
                st.append(ast)
            else:
                while st and 0 < st[-1] < -ast:
                    st.pop()
                if st and st[-1] > 0 and st[-1] == -ast:
                    st.pop()
                elif not st or st[-1] < 0:
                    st.append(ast)
        return st

print(Solution().asteroidCollision(asteroids = [-5,10,-5, -10]))